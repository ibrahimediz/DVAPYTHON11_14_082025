import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Dash uygulamasını başlat
app = dash.Dash(__name__)

# Yapay veri oluşturma
np.random.seed(42)
tarihler = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
musteri_sayisi = 1000

# Müşteri demografik verisi
cinsiyet = np.random.choice(['Erkek', 'Kadın'], size=musteri_sayisi, p=[0.48, 0.52])
yas = np.random.normal(loc=35, scale=10, size=musteri_sayisi)
yas = np.clip(yas, 18, 70).astype(int)

# Satış verisi
satis_verisi = []
for tarih in tarihler:
    gunluk_musteri = np.random.randint(50, 150)
    musteriler = np.random.choice(musteri_sayisi, size=gunluk_musteri, replace=False)

    for musteri in musteriler:
        satin_alma = np.random.binomial(n=1, p=0.3)
        if satin_alma:
            urun_sayisi = np.random.poisson(lam=1.5)
            toplam_tutar = np.sum(np.random.normal(loc=150, scale=50, size=urun_sayisi))
            satis_verisi.append([
                tarih,
                musteri,
                cinsiyet[musteri],
                yas[musteri],
                urun_sayisi,
                toplam_tutar
            ])

# DataFrame oluşturma
satis_df = pd.DataFrame(satis_verisi, columns=[
    'Tarih', 'Müşteri_ID', 'Cinsiyet', 'Yaş', 'Ürün_Sayısı', 'Toplam_Tutar'
])

# İllere göre satış verisi (basitleştirilmiş)
iller = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana', 'Konya', 'Gaziantep']
satis_df['İl'] = np.random.choice(iller, size=len(satis_df))

# Temel metrikler hesaplama
toplam_satis = satis_df['Toplam_Tutar'].sum()
ortalama_siparis_degeri = satis_df.groupby('Müşteri_ID')['Toplam_Tutar'].mean().mean()
musteri_sayisi = satis_df['Müşteri_ID'].nunique()
aylik_satis = satis_df.groupby(satis_df['Tarih'].dt.to_period('M')).agg({'Toplam_Tutar': 'sum'}).reset_index()
aylik_satis['Tarih'] = aylik_satis['Tarih'].dt.to_timestamp()

# Uygulama layout'u
app.layout = html.Div([
    html.H1("E-Ticaret Analiz Panosu", style={'text-align': 'center', 'color': '#2c3e50'}),

    # Temel metrikler
    html.Div([
        html.Div([
            html.H3(f"{toplam_satis:,.0f} TL"),
            html.P("Toplam Satış")
        ], className='metric-box', style={'background-color': '#3498db', 'color': 'white'}),

        html.Div([
            html.H3(f"{ortalama_siparis_degeri:.2f} TL"),
            html.P("Ortalama Sipariş Değeri")
        ], className='metric-box', style={'background-color': '#2ecc71', 'color': 'white'}),

        html.Div([
            html.H3(f"{musteri_sayisi:,}"),
            html.P("Toplam Müşteri")
        ], className='metric-box', style={'background-color': '#e74c3c', 'color': 'white'}),

        html.Div([
            html.H3(f"%{np.random.randint(5, 15)}"),
            html.P("Aylık Büyüme")
        ], className='metric-box', style={'background-color': '#f39c12', 'color': 'white'}),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '20px 0'}),

    # Grafikler
    html.Div([
        # Aylık satış trendi
        html.Div([
            dcc.Graph(
                id='aylik-satis',
                figure=px.line(aylik_satis, x='Tarih', y='Toplam_Tutar',
                              title='Aylık Satış Trendi',
                              labels={'Toplam_Tutar': 'Satış Miktarı (TL)', 'Tarih': 'Tarih'})
                .update_traces(line=dict(width=3, color='#2980b9'))
                .update_layout(template='plotly_white')
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # Cinsiyete göre satış
        html.Div([
            dcc.Graph(
                id='cinsiyet-satis',
                figure=px.pie(satis_df, names='Cinsiyet', values='Toplam_Tutar',
                             title='Cinsiyete Göre Satış Dağılımı',
                             hole=0.4)
                .update_traces(textposition='inside', textinfo='percent+label')
                .update_layout(template='plotly_white')
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
    ], style={'margin': '10px 0'}),

    html.Div([
        # Yaş dağılımı
        html.Div([
            dcc.Graph(
                id='yas-dagilim',
                figure=px.histogram(satis_df, x='Yaş', nbins=20,
                                   title='Müşteri Yaş Dağılımı',
                                   labels={'Yaş': 'Yaş', 'count': 'Müşteri Sayısı'})
                .update_layout(template='plotly_white')
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # İl bazında satış
        html.Div([
            dcc.Graph(
                id='il-satis',
                figure=px.bar(satis_df.groupby('İl')['Toplam_Tutar'].sum().reset_index(),
                             x='İl', y='Toplam_Tutar',
                             title='İl Bazında Satış Performansı',
                             labels={'Toplam_Tutar': 'Satış Miktarı (TL)', 'İl': 'İl'})
                .update_layout(template='plotly_white')
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
    ], style={'margin': '10px 0'}),

    # Detaylı filtreleme
    html.Div([
        html.Label("Tarih Aralığı Seçin:", style={'font-weight': 'bold'}),
        dcc.DatePickerRange(
            id='tarih-araligi',
            start_date=satis_df['Tarih'].min(),
            end_date=satis_df['Tarih'].max(),
            display_format='DD.MM.YYYY'
        ),

        html.Label("Cinsiyet Filtresi:", style={'margin-left': '20px', 'font-weight': 'bold'}),
        dcc.Dropdown(
            id='cinsiyet-filtre',
            options=[{'label': c, 'value': c} for c in satis_df['Cinsiyet'].unique()],
            value=satis_df['Cinsiyet'].unique().tolist(),
            multi=True
        ),
    ], style={'padding': '20px', 'background-color': '#f8f9fa', 'border-radius': '5px'}),

    # Detaylı analiz grafiği
    html.Div([
        dcc.Graph(id='detayli-analiz')
    ], style={'margin-top': '20px'})
], style={'font-family': 'Arial, sans-serif', 'padding': '20px'})

# Detaylı analiz grafiği için callback
@app.callback(
    Output('detayli-analiz', 'figure'),
    [Input('tarih-araligi', 'start_date'),
     Input('tarih-araligi', 'end_date'),
     Input('cinsiyet-filtre', 'value')]
)
def update_detailed_analysis(start_date, end_date, selected_genders):
    # Veriyi filtrele
    filtered_df = satis_df[
        (satis_df['Tarih'] >= start_date) &
        (satis_df['Tarih'] <= end_date) &
        (satis_df['Cinsiyet'].isin(selected_genders))
    ]

    # Detaylı analiz grafiği
    fig = px.scatter(filtered_df,
                    x='Yaş',
                    y='Toplam_Tutar',
                    size='Ürün_Sayısı',
                    color='Cinsiyet',
                    title='Yaş ve Harcama İlişkisi',
                    labels={
                        'Yaş': 'Müşteri Yaşı',
                        'Toplam_Tutar': 'Harcama Miktarı (TL)',
                        'Ürün_Sayısı': 'Satın Alınan Ürün Sayısı'
                    })

    fig.update_layout(template='plotly_white')
    return fig

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run_server(debug=True)
