
import pandas as pd
from qualifiers import Qualifier1, Qualifier2, Qualifier3, Qualifier4, Qualifier5, Qualifier6, Qualifier7, Qualifier8, Qualifier9
from loader_results import LoaderResults
import argparse

def get_models_to_load(lang, metric):
    models_to_load_gpt35 = {
        'cr_gpt35': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gpt35_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gpt35_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_gpt35_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    models_to_load_llama3 = {
        'cr_llama3': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_llama3_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_llama3_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_llama3_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    return models_to_load_gpt35, models_to_load_llama3

def load_results(lang, metric):
    models_to_load_gpt35, models_to_load_llama3 = get_models_to_load(lang, metric)
    
    results_gpt35 = LoaderResults()
    results_gpt35.load_results(models_to_load_gpt35)
    gpt35_df = results_gpt35.concat_all_results()

    results_llama3 = LoaderResults()
    results_llama3.load_results(models_to_load_llama3)
    llama3_df = results_llama3.concat_all_results()

    # Concat important fields
    columns_result_gpt35 = ['id_cr_gpt35', 'hardness_cr_gpt35', 'gold_cr_gpt35',
                        'predicted_cr_gpt35', 'score_cr_gpt35',
                        'predicted_cr_gpt35_shot1', 'score_cr_gpt35_shot1',
                        'predicted_cr_gpt35_shot3', 'score_cr_gpt35_shot3',
                        'predicted_cr_gpt35_shot5', 'score_cr_gpt35_shot5']

    columns_result_llama3 =  ['id_cr_llama3', 'hardness_cr_llama3','gold_cr_llama3', 
                            'predicted_cr_llama3', 'score_cr_llama3',
                            'predicted_cr_llama3_shot1', 'score_cr_llama3_shot1',
                            'predicted_cr_llama3_shot3', 'score_cr_llama3_shot3',
                            'predicted_cr_llama3_shot5', 'score_cr_llama3_shot5']

    return gpt35_df[columns_result_gpt35], llama3_df[columns_result_llama3]

def process_results_analyis(perspective: str, metric):
    # Load results
    path_ds = '../dataset/text2sql4pm.tsv'
    dataset = pd.read_csv(path_ds, sep='\t')
    dataset.dropna(how='all', inplace=True)

    gpt35_en, llama3_en = load_results('EN', metric)
    gpt35_pt, llama3_pt = load_results('PT', metric)
    
    if perspective == 'process_mining':
        results_pt = get_results_pm(dataset, gpt35_pt, llama3_pt, metric)
        print('------------PROCESS_MINING QUALIFIERS (PORTUGUESE)-----------------------------------------------------------------\n')
        print_results(results_pt['qualifier1'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results_pt['qualifier2'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results_pt['qualifier9'])
        print('------------------------------------------------------------------------------------------------------\n')

        results_en = get_results_pm(dataset, gpt35_en, llama3_en, metric)
        print('------------PROCESS_MINING QUALIFIERS (ENGLISH)-----------------------------------------------------------------\n')
        print_results(results_en['qualifier1'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results_en['qualifier2'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results_en['qualifier9'])
        print('------------------------------------------------------------------------------------------------------\n')

    elif perspective == 'sql':
        results_pt = get_results_sql(dataset, gpt35_pt, llama3_pt, metric)
        print('------------SQL QUALIFIERS (PORTUGUESE)---------------------------------------------------------------------------\n')
        print_results(results_pt['qualifier8'])
        print('------------------------------------------------------------------------------------------------------\n')
        
        results_en = get_results_sql(dataset, gpt35_en, llama3_en, metric)
        print('------------SQL QUALIFIERS (ENGLISH)---------------------------------------------------------------------------\n')
        print_results(results_en['qualifier8'])
        print('------------------------------------------------------------------------------------------------------\n')
    

    elif perspective == 'nlp':
        results_pt = get_results_nlp(dataset, gpt35_pt, llama3_pt, metric)
        print('------------NLP QUALIFIERS (PORTUGEUESE)----------------------------------------------------------------------------\n')
        print_results(results_pt['qualifier5'])
        print('------------------------------------------------------------------------------------------------------\n')

        results_en = get_results_nlp(dataset, gpt35_en, llama3_en, metric)
        print('------------NLP QUALIFIERS (ENGLISH)----------------------------------------------------------------------------\n')
        print_results(results_en['qualifier5'])
        print('------------------------------------------------------------------------------------------------------\n')
    else:
        print("Perspectiva não reconhecida")


def print_results(qualifier_result):
    rows = []
    keys = qualifier_result['gpt35'][0].index.tolist()
    gpt35 = qualifier_result['gpt35'][1]
    llama3 = qualifier_result['llama3'][1]
    for key in keys:
        total_gpt35 = qualifier_result['gpt35'][0].get(key,0)
        row = {
            '': key,
            'model': 'gpt35',
            'shot-0': format_output(gpt35[0].get(key, 0), total_gpt35),
            'shot-1': format_output(gpt35[1].get(key, 0), total_gpt35),
            'shot-3': format_output(gpt35[2].get(key, 0), total_gpt35),
            'shot-5': format_output(gpt35[3].get(key, 0), total_gpt35)
        }
        rows.append(row)

        total_llama3 = qualifier_result['llama3'][0].get(key,0)
        row = {
            '': key,
            'model': 'llama3',
            'shot-0': format_output(llama3[0].get(key, 0), total_llama3),
            'shot-1': format_output(llama3[1].get(key, 0), total_llama3),
            'shot-3': format_output(llama3[2].get(key, 0), total_llama3),
            'shot-5': format_output(llama3[3].get(key, 0), total_llama3)
        }
        rows.append(row)
        
    # Convert rows into a DataFrame for better formatting
    df = pd.DataFrame(rows)

    # Print the DataFrame
    print(df.to_string(index=False))

def format_output(value, total):
    percentage = 0 if total == 0 else (value / total) * 100
    return f"{percentage:.1f}% ({value}/{total})"


def get_results_pm(dataset, gpt35, llama3, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Domain_value_generic', 'Events_cases_classification', 'Purpose_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds_gpt35 = pd.concat([tmp_dataset, gpt35], axis=1)
    qualifier1_gpt35 = Qualifier1(ds_gpt35)
    qualifier2_gpt35 = Qualifier2(ds_gpt35)
    qualifier9_gpt35 = Qualifier9(ds_gpt35)

    ds_llama3 = pd.concat([tmp_dataset, llama3], axis=1)
    qualifier1_llama3 = Qualifier1(ds_llama3)
    qualifier2_llama3 = Qualifier2(ds_llama3)
    qualifier9_llama3 = Qualifier9(ds_llama3)

    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"

    results = {
        'qualifier1': { 'gpt35': getattr(qualifier1_gpt35, method_name)('gpt35', 'Events_cases_classification'), 'llama3': getattr(qualifier1_llama3, method_name)('llama3', 'Events_cases_classification')},
        'qualifier2': { 'gpt35': getattr(qualifier2_gpt35, method_name)('gpt35', 'Purpose_classification_class'), 'llama3': getattr(qualifier2_llama3, method_name)('llama3', 'Purpose_classification_class')},
        'qualifier9': { 'gpt35': getattr(qualifier9_gpt35, method_name)('gpt35', 'Domain_value_generic'), 'llama3': getattr(qualifier9_llama3, method_name)('llama3', 'Domain_value_generic')}
    }
    return results

def get_results_nlp(dataset, gpt35, llama3, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Wh_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)


    ds_gpt35 = pd.concat([tmp_dataset, gpt35], axis=1)
    qualifier5_gpt35 = Qualifier5(ds_gpt35)

    ds_llama3 = pd.concat([tmp_dataset, llama3], axis=1)
    qualifier5_llama3 = Qualifier5(ds_llama3)
    
    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"
    results = {
        'qualifier5': { 'gpt35': getattr(qualifier5_gpt35, method_name)('gpt35', 'Wh_classification'), 'llama3': getattr(qualifier5_llama3, method_name)('llama3', 'Wh_classification')}
    }
    return results

def get_results_sql(dataset, gpt35, llama3, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Spider_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds_gpt35 = pd.concat([tmp_dataset, gpt35], axis=1)
    qualifier8_gpt35 = Qualifier8(ds_gpt35)

    ds_llama3 = pd.concat([tmp_dataset, llama3], axis=1)
    qualifier8_llama3 = Qualifier8(ds_llama3)
    
    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"    
    results = {
        'qualifier8': { 'gpt35': getattr(qualifier8_gpt35, method_name)('gpt35', 'hardness_cr_gpt35'), 'llama3': getattr(qualifier8_llama3, method_name)('llama3', 'hardness_cr_llama3')}
    }
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--perspective", type=str)
    parser.add_argument("--metric", type=str)

    args = parser.parse_args()


    #execute(args.lang, args.metric, args.sql_complexity, args.file, metric_label)
    process_results_analyis(args.perspective, args.metric)