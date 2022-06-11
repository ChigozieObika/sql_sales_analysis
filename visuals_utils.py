import matplotlib.pyplot as plt

class TopPerformers:
    def __init__(self, df, n=10):
        self.n = n
        self.df = df
        self.df.sort_values(
            by='sum', ascending=False, inplace=True
            )
        self.top_df = self.df.head(n)
    
    def plot_top_n_vs_rest(self, param, vs_rest):
        fig, ax = plt.subplots(figsize =(10, 8), dpi=100)
        not_top_n = len(self.df) - self.n
        sum_not_top_n = self.df['sum'].tail(not_top_n).sum()
        if vs_rest:
            if param=='cities':
                self.top_df.loc[len(self.df.index)]=[
                    'rest_cities', sum_not_top_n
                    ]
                ax.barh(self.top_df['city_id'], self.top_df['sum'])
            if param=='stores':
                self.top_df.loc[len(self.df.index)]=[
                    'rest_stores', 'N/A', sum_not_top_n
                    ]
                ax.barh(self.top_df['store_id'], self.top_df['sum'])
            if param=='products':
                self.top_df.loc[len(self.df.index)]=[
                    'rest_products', sum_not_top_n
                    ]
                ax.barh(self.top_df['product_id'], self.top_df['sum'])
        else:
            if param=='cities':
                ax.barh(self.top_df['city_id'], self.top_df['sum'])
            if param=='stores':
                ax.barh(self.top_df['store_id'], self.top_df['sum'])
            if param=='products':
                ax.barh(self.top_df['product_id'], self.top_df['sum'])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)
        # Add x, y gridlines
        ax.grid(b = 'visible', color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
        
        # Show top values
        ax.invert_yaxis()
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
                    str(round(i.get_width())),
                    fontsize = 12, fontweight ='bold',
                    color ='red')
        if vs_rest:
            plt.savefig(f'plots/Top_{self.n}_{param}_vs_rest.jpg')
            ax.set_title(f'Top {self.n} {param} vs rest',
            fontsize = 14, fontweight ='bold')
        else:
            plt.savefig(f'plots/Top_{self.n}_{param}.jpg')
            ax.set_title(f'Top {self.n} {param}',
            fontsize = 14, fontweight ='bold')
        plt.show()