# Run all results and generate the graphs

echo "Processing easy results"
python main.py --lang=EN --metric=EM --sql_complexity=easy --file=../graphs_results/results_easy_EM.png
python main.py --lang=EN --metric=EX --sql_complexity=easy --file=../graphs_results/results_easy_EX.png
python main.py --lang=PT --metric=EM --sql_complexity=easy --file=../graphs_results/results_easy_EM_pt.png
python main.py --lang=PT --metric=EX --sql_complexity=easy --file=../graphs_results/results_easy_EX_pt.png
echo "Easy results processed"

echo "Processing medium results"
python main.py --lang=EN --metric=EM --sql_complexity=medium --file=../graphs_results/results_medium_EM.png
python main.py --lang=EN --metric=EX --sql_complexity=medium --file=../graphs_results/results_medium_EX.png
python main.py --lang=PT --metric=EM --sql_complexity=medium --file=../graphs_results/results_medium_EM_pt.png
python main.py --lang=PT --metric=EX --sql_complexity=medium --file=../graphs_results/results_medium_EX_pt.png
echo "Medium results processed"

echo "Processing hard results"
python main.py --lang=EN --metric=EM --sql_complexity=hard --file=../graphs_results/results_hard_EM.png
python main.py --lang=EN --metric=EX --sql_complexity=hard --file=../graphs_results/results_hard_EX.png
python main.py --lang=PT --metric=EM --sql_complexity=hard --file=../graphs_results/results_hard_EM_pt.png
python main.py --lang=PT --metric=EX --sql_complexity=hard --file=../graphs_results/results_hard_EX_pt.png
echo "Hard results processed"

echo "Processing extra results"
python main.py --lang=EN --metric=EM --sql_complexity=extra --file=../graphs_results/results_extra_EM.png
python main.py --lang=EN --metric=EX --sql_complexity=extra --file=../graphs_results/results_extra_EX.png
python main.py --lang=PT --metric=EM --sql_complexity=extra --file=../graphs_results/results_extra_EM_pt.png
python main.py --lang=PT --metric=EX --sql_complexity=extra --file=../graphs_results/results_extra_EX_pt.png
echo "Extra results processed"

echo "Processing no hardness results"
python main.py --lang=EN --metric=EM --sql_complexity=no_hardness --file=../graphs_results/results_no_hardness_EM.png
python main.py --lang=EN --metric=EX --sql_complexity=no_hardness --file=../graphs_results/results_no_hardness_EX.png
python main.py --lang=PT --metric=EM --sql_complexity=no_hardness --file=../graphs_results/results_no_hardness_EM_pt.png
python main.py --lang=PT --metric=EX --sql_complexity=no_hardness --file=../graphs_results/results_no_hardness_EX_pt.png
echo "No hardness results processed"