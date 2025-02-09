import pandas as pd
from loader_results import LoaderResults
from utils import calculate_percentages_counts
import argparse


# Concat important fields
columns_result_gpt35 = ['id_cr_gpt35', 'hardness_cr_gpt35', 'gold_cr_gpt35', 
                        'predicted_cr_gpt35', 'score_opr_gpt35', 'score_opr_gpt35_shot1', 'score_cr_gpt35', 
                        'predicted_cr_gpt35_shot1', 'score_cr_gpt35_shot1',
                        'predicted_cr_gpt35_shot3', 'score_cr_gpt35_shot3',
                        'predicted_cr_gpt35_shot5', 'score_cr_gpt35_shot5']

columns_result_gemini10 =  ['id_cr_gemini10', 'hardness_cr_gemini10','gold_cr_gemini10', 
                            'predicted_cr_gemini10', 'score_cr_gemini10', 'score_opr_gemini10', 'score_opr_gemini10_shot1',
                            'predicted_cr_gemini10_shot1', 'score_cr_gemini10_shot1',
                            'predicted_cr_gemini10_shot3', 'score_cr_gemini10_shot3',
                            'predicted_cr_gemini10_shot5', 'score_cr_gemini10_shot5']
columns_result_llama3 =  ['id_cr_llama3', 'hardness_cr_llama3','gold_cr_llama3', 
                            'predicted_cr_llama3', 'score_cr_llama3', 'score_opr_llama3', 'score_opr_llama3_shot1',
                            'predicted_cr_llama3_shot1', 'score_cr_llama3_shot1']
                            #'predicted_cr_llama3_shot3', 'score_cr_llama3_shot3'
                            #'predicted_cr_llama3_shot5', 'score_cr_llama3_shot5']

gpt35_model_results = ['score_opr_gpt35', 'score_opr_gpt35_shot1', 'score_cr_gpt35','score_cr_gpt35_shot1', 'score_cr_gpt35_shot3', 'score_cr_gpt35_shot5']
gemini10_model_results = ['score_opr_gemini10', 'score_opr_gemini10_shot1', 'score_cr_gemini10','score_cr_gemini10_shot1', 'score_cr_gemini10_shot3', 'score_cr_gemini10_shot5']
llama3_model_results = ['score_opr_llama3', 'score_opr_llama3_shot1', 'score_cr_llama3', 'score_cr_llama3_shot1'] #, 'score_cr_llama3_shot3', 'score_cr_llama3_shot5']

def get_models_to_load(lang, metric):
    models_to_load_gpt35 = {
        'opr_gpt35': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'opr_gpt35_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'cr_gpt35': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gpt35_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gpt35_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_gpt35_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    models_to_load_gemini10 = {
        'opr_gemini10': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'opr_gemini10_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'cr_gemini10': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gemini10_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gemini10_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_gemini10_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    models_to_load_llama3 = {
        'opr_llama3': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'opr_llama3_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'cr_llama3': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_llama3_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric}
    }

    return models_to_load_gpt35, models_to_load_gemini10, models_to_load_llama3

def calculate_percentages(gpt35_results, gemini10_results, llama3_results, metric):
    gpt35_percentages = calculate_percentages_counts(gpt35_results, gpt35_model_results, metric)
    gemini10_percentages = calculate_percentages_counts(gemini10_results, gemini10_model_results, metric)
    llama3_percentages = calculate_percentages_counts(llama3_results, llama3_model_results, metric)

    return gpt35_percentages, gemini10_percentages, llama3_percentages

def compare(lang, metric):
    path_ds = '../dataset/text2sql4pm.tsv'
    df_dataset = pd.read_csv(path_ds, sep='\t')
    df_dataset.dropna(how='all', inplace=True)

    filters_columns = df_dataset[['Group_id', 'Utterance_id', 'Base_paraphrase','Domain_value_generic', 'English_utterance', 'Events_cases_classification', 'Projection_classification', 
                      'Condition_classification', 'Condition_group_classification', 'Projection_aggregation',
                      'Groupby', 'IUEN', 'Subselect_condition', 'Subselect_having', 'Subselect_from', 
                      'Subselect_with']]
    filters_columns = filters_columns.reset_index(drop=True)
    
    models_to_load_gpt35, models_to_load_gemini10, models_to_load_llama3 = get_models_to_load(lang, metric)
    
    results_gpt35 = LoaderResults()
    results_gpt35.load_results(models_to_load_gpt35)
    gpt35_df = results_gpt35.concat_all_results()

    results_gemini10 = LoaderResults()
    results_gemini10.load_results(models_to_load_gemini10)
    gemini10_df = results_gemini10.concat_all_results()

    results_llama3 = LoaderResults()
    results_llama3.load_results(models_to_load_llama3)
    llama3_df = results_llama3.concat_all_results()

    gpt35_results = pd.concat([filters_columns, gpt35_df[columns_result_gpt35]], axis=1)
    gemini10_results = pd.concat([filters_columns, gemini10_df[columns_result_gemini10]], axis=1)
    llama3_results = pd.concat([filters_columns, llama3_df[columns_result_llama3]], axis=1)

    if metric == "EM":
        gpt35_results = gpt35_results.query('hardness_cr_gpt35 != "no_hardness"')
        gemini10_results = gemini10_results.query('hardness_cr_gemini10 != "no_hardness"')
        llama3_results = llama3_results.query('hardness_cr_llama3 != "no_hardness"')
        

    gpt35_percentages, gemini10_percentages, llama3_percentages = calculate_percentages(gpt35_results, gemini10_results, llama3_results, metric)
    
    print(gpt35_percentages)
    print(gemini10_percentages)
    print(llama3_percentages)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--metric", type=str)
    parser.add_argument("--lang", type=str)
    #parser.add_argument("--file", type=str)

    args = parser.parse_args()

#    if args.metric == "EX":
#        metric_label = 'Execution Acc. (%)'
#    else:
#        metric_label = 'Exact Match Acc. (%)'

    compare(args.lang, args.metric)