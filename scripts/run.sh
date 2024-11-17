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

echo "Hard results processed"


echo "Processing extra results"
echo "Extra results processed"


echo "Processing no hardness results"

echo "No hardness results processed"