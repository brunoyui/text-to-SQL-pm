import pandas as pd
from loader_results import LoaderResults
from utils import calculate_percentages_counts
import argparse
from graphs_plot import plot_and_save_graph_results_by_model

results_c = {
    'GPT-3.5 Turbo': ['score_cr_gpt35', 'score_cr_gpt35_shot1','score_cr_gpt35_shot3', 
              'score_cr_gpt35_shot5'],
    'Gemini-1.0 Pro': ['score_cr_gemini10', 'score_cr_gemini10_shot1', 'score_cr_gemini10_shot3', 
              'score_cr_gemini10_shot5'],
    'Llama3-8B Instuct': ['score_cr_llama3', 'score_cr_llama3_shot1', 'score_cr_llama3_shot3', 'score_cr_llama3_shot5']
}

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
                            'predicted_cr_llama3_shot1', 'score_cr_llama3_shot1',
                            'predicted_cr_llama3_shot3', 'score_cr_llama3_shot3',
                            'predicted_cr_llama3_shot5', 'score_cr_llama3_shot5']
#'score_opr_gpt35', 'score_opr_gpt35_shot1', 
#'score_opr_gemini10', 'score_opr_gemini10_shot1', 
#'score_opr_llama3', 'score_opr_llama3_shot1', 
#gpt35_model_results = ['score_cr_gpt35','score_cr_gpt35_shot1', 'score_cr_gpt35_shot3', 'score_cr_gpt35_shot5']
#gemini10_model_results = ['score_cr_gemini10','score_cr_gemini10_shot1', 'score_cr_gemini10_shot3', 'score_cr_gemini10_shot5']
#llama3_model_results = ['score_cr_llama3', 'score_cr_llama3_shot1', 'score_cr_llama3_shot3', 'score_cr_llama3_shot5']

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
        'cr_llama3_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_llama3_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_llama3_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    return models_to_load_gpt35, models_to_load_gemini10, models_to_load_llama3

#def calculate_percentages(gpt35_results, gemini10_results, llama3_results, metric):
#    gpt35_percentages = calculate_percentages_counts(gpt35_results, gpt35_model_results, metric)
#    gemini10_percentages = calculate_percentages_counts(gemini10_results, gemini10_model_results, metric)
#    llama3_percentages = calculate_percentages_counts(llama3_results, llama3_model_results, metric)

#    return gpt35_percentages, gemini10_percentages, llama3_percentages

def calculate_percentages(df_models):
        percentages = {}
        
        for k, metric in df_models.items():
            percentages[k] = {}
            for m, lang in metric.items():
                percentages[k][m] = {}
                for l, mm in lang.items():
                    percentage_models = calculate_percentages_counts(mm, results_c[l], k)    
                    percentages[k][m][l] = percentage_models
        return percentages

def compare(file):
    path_ds = '../dataset/text2sql4pm.tsv'
    df_dataset = pd.read_csv(path_ds, sep='\t')
    df_dataset.dropna(how='all', inplace=True)

    filters_columns = df_dataset[['Group_id', 'Utterance_id', 'Base_paraphrase','Domain_value_generic', 'English_utterance', 'Events_cases_classification', 'Projection_classification', 
                      'Condition_classification', 'Condition_group_classification', 'Projection_aggregation',
                      'Groupby', 'IUEN', 'Subselect_condition', 'Subselect_having', 'Subselect_from', 
                      'Subselect_with']]
    filters_columns = filters_columns.reset_index(drop=True)
    
    models_to_load_gpt35_en_em, models_to_load_gemini10_en_em, models_to_load_llama3_en_em = get_models_to_load('EN', 'EM')
    models_to_load_gpt35_en_ex, models_to_load_gemini10_en_ex, models_to_load_llama3_en_ex = get_models_to_load('EN', 'EX')
    models_to_load_gpt35_pt_em, models_to_load_gemini10_pt_em, models_to_load_llama3_pt_em = get_models_to_load('PT', 'EM')
    models_to_load_gpt35_pt_ex, models_to_load_gemini10_pt_ex, models_to_load_llama3_pt_ex = get_models_to_load('PT', 'EX')

    # EM english
    results_gpt35_en_em = LoaderResults()
    results_gpt35_en_em.load_results(models_to_load_gpt35_en_em)
    gpt35_df_en_em = results_gpt35_en_em.concat_all_results().query('hardness_cr_gpt35 != "no_hardness"')

    results_gemini10_en_em = LoaderResults()
    results_gemini10_en_em.load_results(models_to_load_gemini10_en_em)
    gemini10_df_en_em = results_gemini10_en_em.concat_all_results().query('hardness_cr_gemini10 != "no_hardness"')

    results_llama3_en_em = LoaderResults()
    results_llama3_en_em.load_results(models_to_load_llama3_en_em)
    llama3_df_en_em = results_llama3_en_em.concat_all_results().query('hardness_cr_llama3 != "no_hardness"')

    # EM portuguese
    results_gpt35_pt_em = LoaderResults()
    results_gpt35_pt_em.load_results(models_to_load_gpt35_pt_em)
    gpt35_df_pt_em = results_gpt35_pt_em.concat_all_results().query('hardness_cr_gpt35 != "no_hardness"')

    results_gemini10_pt_em = LoaderResults()
    results_gemini10_pt_em.load_results(models_to_load_gemini10_pt_em)
    gemini10_df_pt_em = results_gemini10_pt_em.concat_all_results().query('hardness_cr_gemini10 != "no_hardness"')

    results_llama3_pt_em = LoaderResults()
    results_llama3_pt_em.load_results(models_to_load_llama3_pt_em)
    llama3_df_pt_em = results_llama3_pt_em.concat_all_results().query('hardness_cr_llama3 != "no_hardness"')

    # EX english
    results_gpt35_en_ex = LoaderResults()
    results_gpt35_en_ex.load_results(models_to_load_gpt35_en_ex)
    gpt35_df_en_ex = results_gpt35_en_ex.concat_all_results()

    results_gemini10_en_ex = LoaderResults()
    results_gemini10_en_ex.load_results(models_to_load_gemini10_en_ex)
    gemini10_df_en_ex = results_gemini10_en_ex.concat_all_results()

    results_llama3_en_ex = LoaderResults()
    results_llama3_en_ex.load_results(models_to_load_llama3_en_ex)
    llama3_df_en_ex = results_llama3_en_ex.concat_all_results()

    # EX portuguese
    results_gpt35_pt_ex = LoaderResults()
    results_gpt35_pt_ex.load_results(models_to_load_gpt35_pt_ex)
    gpt35_df_pt_ex = results_gpt35_pt_ex.concat_all_results()

    results_gemini10_pt_ex = LoaderResults()
    results_gemini10_pt_ex.load_results(models_to_load_gemini10_pt_ex)
    gemini10_df_pt_ex = results_gemini10_pt_ex.concat_all_results()

    results_llama3_pt_ex = LoaderResults()
    results_llama3_pt_ex.load_results(models_to_load_llama3_pt_ex)
    llama3_df_pt_ex = results_llama3_pt_ex.concat_all_results()

    df_models = {
        'EM': {
            'PT': {
                'GPT-3.5 Turbo': gpt35_df_pt_em,
                'Gemini-1.0 Pro': gemini10_df_pt_em,
                'Llama3-8B Instuct': llama3_df_pt_em
            },
            'EN': {
                'GPT-3.5 Turbo': gpt35_df_en_em,
                'Gemini-1.0 Pro': gemini10_df_en_em,
                'Llama3-8B Instuct': llama3_df_en_em
            }
        },
        'EX': {
            'PT': {
                'GPT-3.5 Turbo': gpt35_df_pt_ex,
                'Gemini-1.0 Pro': gemini10_df_pt_ex,
                'Llama3-8B Instuct': llama3_df_pt_ex
            },
            'EN': {
                'GPT-3.5 Turbo': gpt35_df_en_ex,
                'Gemini-1.0 Pro': gemini10_df_en_ex,
                'Llama3-8B Instuct': llama3_df_en_ex
            }
        }
    }

    percentages = calculate_percentages(df_models)
    print(percentages)
    plot_and_save_graph_results_by_model(percentages, file)
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument("--metric", type=str)
    #parser.add_argument("--lang", type=str)
    parser.add_argument("--file", type=str)

    args = parser.parse_args()

#    if args.metric == "EX":
#        metric_label = 'Execution Acc. (%)'
#    else:
#        metric_label = 'Exact Match Acc. (%)'

    compare(args.file)