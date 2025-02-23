import matplotlib.pyplot as plt

def plot_and_save_graph_results(data, data1, file, categories, x_pos, x_positions, ax_text_pos, ax1_text_pos, ay_ticks, ay_ticks1, hspace, legend_anchor, fig_size, metric_label):
    fig, (ax, ax1) = plt.subplots(2,1, figsize=fig_size)
    
    categories_qtd = len(categories)
    labels = ['GPT-3.5 Turbo - OpenAI Repr.', 'GPT-3.5 Turbo - Code Repr.', 
              'Gemini-1.0 - OpenAI Repr.', 'Gemini-1.0 - Code Repr.',
              'Llama3-8B - OpenAI Repr.', 'Llama3-8B - Code Repr.']

    colors = ['#66BB6A', '#4CAF50',  # Vibrant Green, Medium Green
              '#FFA726', '#FF9800',  # Vibrant Orange, Medium Orange
              '#42A5F5', '#2196F3']  # Vibrant Blue, Medium Blue
    bar_width = 0.3
    
    colors = colors * categories_qtd
        
    # Create first bar chart
    #ax.bar(x_pos, data, width=bar_width, color=colors, label=labels*categories_qtd)
    
    # Plot bars
    bars = []
    for i, category in enumerate(labels*categories_qtd):
        bar = ax.bar(x_pos[i], data[i], width=bar_width, color=colors[i])
        bars.append(bar)
    
    ax.grid(color='#D3D3D3', linestyle='--', linewidth=0.15)

    for i, counts, in enumerate(data):
        ax.text(x_pos[i], data[i] + 2, counts, ha='center', fontsize=8)

    # Set y-axis control ticks
    ax.set_yticks(ay_ticks)
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(categories, fontsize=20)

    # Add title and labels
    # Add labels and title
    ax.set_ylabel(metric_label, fontsize=20)
    ax.text(0, ax_text_pos, "0-shot", fontsize=20,  weight='bold')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)


    # Add legend
    ax.legend(bars, ncol=3, bbox_to_anchor=legend_anchor, frameon=False, labels=labels, fontsize=16)
    
    # Create second bar chart
    ax1.bar(x_pos, data1, width=bar_width, color=colors)
    ax1.grid(color='#D3D3D3', linestyle='--', linewidth=0.15)

    for i, counts, in enumerate(data1):
        ax1.text(x_pos[i], data1[i] + 2, counts, ha='center', fontsize=8)
    
    # Set y-axis control ticks
    ax1.set_yticks(ay_ticks1)
    ax1.tick_params(axis='y', labelsize=20)
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(categories, fontsize=20)

    # Add title and labels
    # Add labels and title
    ax1.set_ylabel(metric_label, fontsize=20)
    ax1.text(0, ax1_text_pos, "1-shot", fontsize=20,  weight='bold')

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)  
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.subplots_adjust(hspace)
    plt.savefig(file, format='png', bbox_inches='tight')

def plot_and_save_graph_results_by_model(data, file):
       
    fig, axes = plt.subplots(2, 2, figsize=(10, 12))  # 1 row, 2 columns
    fig.text(0.2, 0.98, 'Medida estrutural (EM)', ha='center', va='center', fontsize=16)
    fig.text(0.22, 0.46, 'Medida de execução (EX)', ha='center', va='center', fontsize=16)

    x_values = [0, 1, 3, 5]    
    # Plot for EM data
    for key, value in data['EM']['PT'].items():
        axes[0][0].plot(x_values, value, marker='o', label=key)

    for key, value in data['EM']['EN'].items():
        axes[0][1].plot(x_values, value, marker='o', label=key)

    # Plot for EX data
    for key, value in data['EX']['PT'].items():
        axes[1][0].plot(x_values, value, marker='o', label=key)

    for key, value in data['EX']['EN'].items():
        axes[1][1].plot(x_values, value, marker='o', label=key)

    # Config default
    axes[0][0].set_title('Português')
    axes[0][1].set_title('Inglês')
    axes[1][0].set_title('Português')
    axes[1][1].set_title('Inglês')
    for i in range(0, 2):
        for j in range(0, 2):
            axes[i][j].set_yticks(range(0, 110, 20))
            axes[i][j].set_xlabel('Shots', fontsize=12)
            axes[i][j].set_xticks([0, 1, 3, 5])
            axes[i][j].tick_params(axis='y', labelsize=12)
            axes[i][j].tick_params(axis='x', labelsize=12)
            axes[i][j].grid(color='gray', linestyle='--', linewidth=0.5)

    bars = []
    axes[0][0].set_ylabel('Porcentagem (%)', fontsize=12)
    axes[1][0].set_ylabel('Porcentagem (%)', fontsize=12)
    legend_anchor = (0.5, 0.0)
    axes[0][1].legend(bars, ncol=3, bbox_to_anchor=(1.0, 1.25), frameon=False, 
        labels=data['EX']['PT'].keys(), fontsize=10)
  

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.subplots_adjust(hspace=0.4) 
    plt.savefig(file, format='png', bbox_inches='tight')

def plot_and_save_graph_results_no_hardness(data, file):
       
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))  # 1 row, 2 columns
    fig.text(0.22, 0.89, 'Medida de execução (EX)', ha='center', va='center', fontsize=16)

    x_values = [0, 1, 3, 5]    
    
    # Plot for EX data
    for key, value in data['EX']['PT'].items():
        axes[0].plot(x_values, value, marker='o', label=key)

    for key, value in data['EX']['EN'].items():
        axes[1].plot(x_values, value, marker='o', label=key)

    # Config default
    axes[0].set_title('Português')
    axes[1].set_title('Inglês')
    for i in range(0, 2):
        axes[i].set_yticks(range(0, 110, 20))
        axes[i].set_xlabel('Shots', fontsize=12)
        axes[i].set_xticks([0, 1, 3, 5])
        axes[i].tick_params(axis='y', labelsize=12)
        axes[i].tick_params(axis='x', labelsize=12)
        axes[i].grid(color='gray', linestyle='--', linewidth=0.5)

    bars = []
    axes[0].set_ylabel('Porcentagem (%)', fontsize=12)
    axes[1].legend(bars, ncol=3, bbox_to_anchor=(1.0, 1.35), frameon=False, 
        labels=data['EX']['PT'].keys(), fontsize=8)
  

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.savefig(file, format='png', bbox_inches='tight')

def plot_graphs_pm(stats, file):
    # Pre-init
    values_base_u = list(stats['qualifier1'][4]) + list(stats['qualifier2'][4]) + list(stats['qualifier9'][4])
    percentages_base_u = stats['qualifier1'][5] + stats['qualifier2'][5] + stats['qualifier9'][5]
    #percentages_base_p = stats['qualifier1'][3] + stats['qualifier2'][3] + stats['qualifier9'][3]
    values_projection_u = list(stats['qualifier3'][4])
    percentages_projection_u = stats['qualifier3'][5]
    #percentages_projection_p = stats['qualifier3'][3]
    values_condition_u = list(stats['qualifier4'][4])
    percentages_condition_u = stats['qualifier4'][5]
    #percentages_condition_p = stats['qualifier4'][3]

    #percentages_base_u = [round(x, 1) for x in percentages_base_u]
    #percentages_base_p = [round(x, 1) for x in percentages_base_p]
    #percentages_projection_u = [round(x, 1) for x in percentages_projection_u]
    #percentages_projection_p = [round(x, 1) for x in percentages_projection_p]
    #percentages_condition_u = [round(x, 1) for x in percentages_condition_u]
    #percentages_condition_p = [round(x, 1) for x in percentages_condition_p]

    final_u = []
    final_projection_u = []
    final_condition_u = []
    for (percentage, value) in zip(percentages_base_u, values_base_u):
      final_u.append(f"{percentage:.1f}\n({value})")

    for (percentage, value) in zip(percentages_projection_u, values_projection_u):
      final_projection_u.append(f"{percentage:.1f}\n({value})")

    for (percentage, value) in zip(percentages_condition_u, values_condition_u):
      final_condition_u.append(f"{percentage:.1f}\n({value})")
    
    fig, (ax, ax1, ax2) = plt.subplots(3, 1,figsize=(14, 8))

    ## GRAPH 1
    # Define data
    categories = ['nível\nevento', 'nível\ncaso', 'perspectiva', 'estatística\ndescr.', 'conformidade', 'valor', 'genérico', 'domínio']
    x_pos = [0, 1, 3, 4, 5, 7, 8, 9]

    bar_width = 0.40

    # Create bar chart
    ax.bar(x_pos, percentages_base_u, width=bar_width)
    #ax.bar([i + 0.125 + bar_width for i in x_pos], percentages_base_p, width=bar_width, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')

    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_u):
        print(counts)
        ax.text(x_pos[i], percentages_base_u[i] + 10, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(percentages_base_p):
    #    ax.text(x_pos[i]+ 0.125 + bar_width, percentages_base_p[i] + 4, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax.set_ylabel('Porcentagem', fontsize=11)
    #ax.set_title('Process mining qualifiers comparison', fontsize=14)

    # Add legend
    ax.legend(loc="upper center", ncol = 2, bbox_to_anchor=(0.46, 1.8), frameon=False)

    # Set ticks and labels for x-axis
    ax.set_xticks([i + bar_width / 16 for i in x_pos])
    ax.set_xticklabels(categories, fontsize=10)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Add text
    ax.text(0.2, 120, "Qualificador 1", fontsize=12)
    ax.text(3.5, 120, "Qualificador 2", fontsize=12)
    ax.text(7.5, 120, "Qualificador 9", fontsize=12)


    #PROJECTION
    # Define data
    categories_p = ['caso', 'evento', 'recurso', 'atividade', 'timestamp', 'custo']
    x_pos_p = [0,1,2,3,4,5]

    bar_width_p = 0.20
    # Create bar chart
    ax1.bar(x_pos_p, percentages_projection_u, width=bar_width_p)
    #ax1.bar([i + 0.05 + bar_width_p for i in x_pos_p], percentages_projection_p, width=bar_width_p, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')


    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax1.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax1.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_projection_u):
        ax1.text(x_pos_p[i], percentages_projection_u[i] + 10, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(percentages_projection_p):
    #    ax1.text(x_pos_p[i] + 0.05 + bar_width_p, percentages_projection_p[i] + 4, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax1.set_ylabel('Porcentagem', fontsize=11)
    #ax.set_title('Process mining projection qualifier', fontsize=14)

    # Add legend
    #ax.legend(loc='upper center', ncol=2)

    # Set ticks and labels for x-axis
    ax1.set_xticks([i + bar_width_p / 16 for i in x_pos_p])
    ax1.set_xticklabels(categories_p, fontsize=10)

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    ax1.text(2, 120, "Qualificador 3", fontsize=12)

    #CONDITION
    categories_w = ['actividade', 'nenhum', 'timestamp', 'recurso', 'custo', 'caso']
    x_pos_w = [0,1,2,3,4,5]

    bar_width_w = 0.20
    # Create bar chart
    ax2.bar(x_pos_w, percentages_condition_u, width=bar_width_w)
    #ax2.bar([i + 0.05 + bar_width_w for i in x_pos_w], percentages_condition_p, width=bar_width_w, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')


    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax2.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax2.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_condition_u):
        ax2.text(x_pos_w[i], percentages_condition_u[i] + 10, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(percentages_condition_p):
    #    ax2.text(x_pos_w[i]+ 0.05 +bar_width_w, percentages_condition_p[i] + 4, counts, ha='center', fontsize=10.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax2.set_ylabel('Porcentagem', fontsize=11)
    #ax.set_title('Process mining condition qualifier', fontsize=14)

    # Add legend


    # Set ticks and labels for x-axis
    ax2.set_xticks([i + bar_width_w / 16 for i in x_pos_w])
    ax2.set_xticklabels(categories_w)


    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    ax2.text(2, 120, "Qualificador 4", fontsize=12)

    # Show plot
    plt.subplots_adjust(hspace=0.95)
    plt.savefig(file, format='png', bbox_inches='tight')

def plot_graphs_nlp(stats, file):
    # Pre-init
    values_question_u = list(stats['qualifier5'][4])
    wh_question_u_percentages = stats['qualifier5'][5]
    #wh_question_p_percentages = stats['qualifier5'][3]
    
    #wh_question_u_percentages = [round(x, 1) for x in wh_question_u_percentages] + [0, 0]
    #wh_question_p_percentages = [round(x, 1) for x in wh_question_p_percentages
    final_u = []
    for (percentage, value) in zip(wh_question_u_percentages, values_question_u):
      final_u.append(f"{percentage:.1f}\n({value})")

    fig, ax = plt.subplots(figsize=(10, 1.5))

    # Define data
    categories = ['quanto\n(how)', 'o que/qual\n(what)', 'nenhum', 'qual\n(which)', 'quem\n(who)', 'quando\n(when)']
    x_pos = [0,1,2,3,4,5]

    bar_width = 0.20
    # Create bar chart
    ax.bar(x_pos, wh_question_u_percentages, width=bar_width)
    #ax.bar([i + 0.05 + bar_width for i in x_pos], wh_question_p_percentages, width=bar_width, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')


    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_u):
        ax.text(x_pos[i], wh_question_u_percentages[i] + 10, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(wh_question_p_percentages):
    #    ax.text(x_pos[i]+ 0.05 +bar_width, wh_question_p_percentages[i] + 4, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax.set_ylabel('Porcentagem', fontsize=12)
    #ax.set_title('Process mining projection and condition qualifier', fontsize=14)

    # Add legend
    #ax.legend(loc="upper center", ncol = 2, bbox_to_anchor=(0.5, 1.8), frameon=False)

    # Set ticks and labels for x-axis
    ax.set_xticks([i + bar_width / 16 for i in x_pos])
    ax.set_xticklabels(categories)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.text(2, 110, "Qualificador 5", fontsize=12)

    # Show plot
    plt.savefig(file, format='png', bbox_inches='tight')

def plot_graphs_sql(stats, file):

    # Pre-init
    values_group_agg_u = list(stats['qualifier6'][4]) + list(stats['qualifier7'][4])
    percentages_group_agg_u = stats['qualifier6'][5] + stats['qualifier7'][5]
    #percentages_group_agg_p = stats['qualifier6'][3] + stats['qualifier7'][3]
    values_spider_u = list(stats['qualifier8'][4])
    percentages_spider_u = stats['qualifier8'][5]
    #percentages_spider_p = stats['qualifier8'][3]
    
    #percentages_group_agg_u = [round(x, 1) for x in percentages_group_agg_u]
    #percentages_group_agg_p = [round(x, 1) for x in percentages_group_agg_p]
    #percentages_spider_u = [round(x, 1) for x in percentages_spider_u]
    #percentages_spider_p = [round(x, 1) for x in percentages_spider_p]

    final_u = []
    for (percentage, value) in zip(percentages_group_agg_u, values_group_agg_u):
      final_u.append(f"{percentage:.1f}\n({value})")

    final_spider_u = []
    for (percentage, value) in zip(percentages_spider_u, values_spider_u):
      final_spider_u.append(f"{percentage:.1f}\n({value})")

    fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(10, 3.5))

    # Define data
    categories_group_agg = ['nenhum', 'agregação', 'nenhum', 'having']
    x_pos_group_agg = [1,1.5,3,3.5]


    bar_width_g = 0.14
    # Create bar chart
    ax1.bar(x_pos_group_agg, percentages_group_agg_u, width=bar_width_g)
    #ax1.bar([i + 0.05 + bar_width_g for i in x_pos_group_agg], percentages_group_agg_p, width=bar_width_g, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')


    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax1.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax1.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_u):
        ax1.text(x_pos_group_agg[i], percentages_group_agg_u[i] + 10, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(percentages_group_agg_p):
    #    ax1.text(x_pos_group_agg[i]+ 0.05 + bar_width_g, percentages_group_agg_p[i] + 4, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax1.set_ylabel('Porcentagem', fontsize=12)
    #ax.set_title('Process mining projection and condition qualifier', fontsize=14)

    # Add legend
    ax1.legend(loc="upper center", ncol = 2, bbox_to_anchor=(0.5, 1.5), frameon=False)

    # Set ticks and labels for x-axis
    ax1.set_xticks([i + bar_width_g / 16 for i in x_pos_group_agg])
    ax1.set_xticklabels(categories_group_agg)

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    ax1.text(1, 130, "Qualificador 6", fontsize=12)
    ax1.text(3, 130, "Qualificador 7", fontsize=12)


    # Define data
    categories = ['médio', 'sem classificação', 'fácil', 'difícil', 'super difícil']
    x_pos = [0,1,2,3,4]

    bar_width = 0.2
    # Create bar chart
    ax2.bar(x_pos, percentages_spider_u, width=bar_width)
    #ax2.bar([i + 0.05 + bar_width for i in x_pos], percentages_spider_p, width=bar_width, color='darkgray', label='Paraphrases')
    #ax.bar([i + bar_width*2 for i in x_pos], percentages_base_a, width=bar_width, color='gray', label='Base + Paraphrases')


    #ax1.bar(categories_domain, percentages_domain, width=barWidth, color='gray')
    ax2.grid(color='grey', linestyle='--', linewidth=0.15)

    # Set y-axis control ticks
    ax2.set_yticks(range(0, 110, 20))

    # Add percentage labels
    for i, counts, in enumerate(final_spider_u):
        ax2.text(x_pos[i], percentages_spider_u[i] + 10, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(percentages_spider_p):
    #    ax2.text(x_pos[i]+ 0.05 + bar_width, percentages_spider_p[i] + 4, counts, ha='center', fontsize=8.5)

    #for i, counts, in enumerate(counts_base_a):
    #    ax.text(x_pos[i]+ bar_width*2, percentages_base_a[i] + 1, counts, ha='center', fontsize=6.5)


    # Add title and labels
    # Add labels and title
    ax2.set_ylabel('Porcentagem', fontsize=12)
    #ax.set_title('Process mining projection and condition qualifier', fontsize=14)

    # Add legend
    #ax2.legend(loc="upper center", ncols = 2, bbox_to_anchor=(0.5, 1.5), frameon=False)

    # Set ticks and labels for x-axis
    ax2.set_xticks([i + bar_width / 16 for i in x_pos])
    ax2.set_xticklabels(categories)

    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    ax2.text(1.7, 110, "Qualificador 8", fontsize=12)
    plt.subplots_adjust(hspace=0.55)

    # Show plot
    plt.savefig(file, format='png', bbox_inches='tight')
