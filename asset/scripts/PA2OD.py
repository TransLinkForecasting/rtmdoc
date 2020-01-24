import inro.modeller as _m
import inro.emme.desktop as _d
import csv
import os
import multiprocessing
import numpy as np
import pandas as pd
import sqlite3
import traceback as _traceback


# Should be run from modeler shell or notebook

def sum_mats(eb, mat_list):
    util = _m.Modeller().tool("translink.util")
    NoTAZ = len(util.get_matrix_numpy(eb, "zoneindex"))
    out_mat = np.empty([NoTAZ, NoTAZ])

    for mat in mat_list:
        # not all modes/incomes for all purposes
        try:
            out_mat += util.get_matrix_numpy(eb, "mf{}".format(mat))
        except:
            out_mat += 0
        
    return out_mat

def get_facs(eb, pa_fac_list):
    util = _m.Modeller().tool("translink.util")

    pa_fac = 0
    for fac in pa_fac_list:
        pa_fac += np.asscalar(util.get_matrix_numpy(eb, "ms{}".format(fac)))
    # PA and AP factors are unbalanced due to trip chaining/NHB trips
    # So calculate total PA factors then assign remaining share to AP
    ap_fac = 1 - pa_fac
    return pa_fac, ap_fac

def pa_to_od(eb, pa_mat, pa_fac_list):

    pa_fac, ap_fac = get_facs(eb, pa_fac_list)
    od_mat = pa_mat * pa_fac + pa_mat.transpose() * ap_fac

    return od_mat 

def generate_od_df(eb, increment_dict, mode_dict, peak_facs, ensem='gy',ensem_agg=True):
    util = _m.Modeller().tool("translink.util")
    counter=0
    for purpose, increment in increment_dict.iteritems():
        for mode, mats in mode_dict.iteritems():
            
            counter += 1
            label = '{}_{}'.format(purpose, mode)
            mat_list = [x + increment for x in mats]
            peaks = [x + increment / 10 for x in peak_facs]

            mat = sum_mats(eb, mat_list)
            # skip purpose/mode combinations that don't exist
            if mat.sum() == 0:
                continue

            # generating output within the loop to keep from killing memory
            df = pd.concat([util.get_pd_ij_df(eb),util.get_ijensem_df(eb, ensem,ensem)], axis=1)
            ensem_i = '{}_i'.format(ensem)
            ensem_j = '{}_j'.format(ensem)
            df[['i','j', ensem_i, ensem_j]] = df[['i','j', ensem_i, ensem_j]].astype(int)

            df[label] = pa_to_od(eb, mat, peaks).flatten()      
            df = pd.melt(df, id_vars=['i','j', ensem_i, ensem_j], var_name = 'purp_mode', value_name = 'trips')           
            
            if not ensem_agg: 
                df['purpose'], df['mode'] = df['purp_mode'].str.split('_', 1).str
                df = df[['i','j','purpose','mode','trips']]
                
                conn = util.get_db_byname(eb, "trip_summaries.db")
                # ensure no double count results if script has already run
                if counter == 1:
                    df.to_sql(name='od_daily', con=conn, flavor='sqlite', index=False, if_exists='replace')
                else:
                    df.to_sql(name='od_daily', con=conn, flavor='sqlite', index=False, if_exists='append')
                   
                conn.close()
                continue

            
            df = df.drop(['i','j'], axis = 1)
            df = df.groupby([ensem_i, ensem_j, 'purp_mode'])
            df = df.sum().reset_index()
            df['purpose'], df['mode'] = df['purp_mode'].str.split('_', 1).str
            df = df[[ensem_i,ensem_j, 'purpose','mode','trips']]
            
            conn = util.get_db_byname(eb, "trip_summaries.db")         
            if counter == 1:
                df.to_sql(name='od_daily_{}'.format(ensem), con=conn, flavor='sqlite', index=False, if_exists='replace')
            else:
                df.to_sql(name='od_daily_{}'.format(ensem), con=conn, flavor='sqlite', index=False, if_exists='append')
            conn.close()

def main(eb, ensem='gy',ensem_agg=True):
    util = _m.Modeller().tool("translink.util")
    mode_dict = {'sov'  : [3000,3001,3002],
                 'hov'  : [3005,3006,3007,3010,3011,3012],
                 'bus'  : [3015],
                 'rail' : [3020],
                 'wce'  : [3025],
                 'walk' : [3030],
                 'bike' : [3035]}

    peak_facs = [400,401,402]

    increment_dict =  {'hbw'    : 000,
                       'hbu'    : 100,
                       'hbsch'  : 200,
                       'hbshop' : 300,
                       'hbpb'   : 400,
                       'hbsoc'  : 500,
                       'hbesc'  : 600,
                       'nhbw'   : 700,
                       'nhbo'   : 800}    

    generate_od_df(eb, increment_dict, mode_dict, peak_facs, ensem, ensem_agg)


if __name__ == '__main__':

    eb = _m.Modeller().emmebank
    # run with ensemble name and ensem_agg = True to aggregat
    # run with no ensemble name and ensem_agg = False to get TAZ level results
    # note, TAZ level results create very large file
    main(eb, ensem='gy', ensem_agg=True)

