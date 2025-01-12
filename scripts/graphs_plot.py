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