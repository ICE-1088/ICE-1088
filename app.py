
import numpy as np
import plotly.graph_objects as go
from dash import dcc, State
from dash import html
from dash_extensions.enrich import MultiplexerTransform, DashProxy, Input, Output
import pandas as pd
import json
import os
import random

#
# pd.set_option('display.max_columns', None)
#
# # need an mapbox access token to successfully run the program
# mapbox_api_token = os.getenv("MAPBOX_ACCESS_TOKEN")

app = DashProxy(prevent_initial_callbacks=True, transforms=[MultiplexerTransform()])
# du.configure_upload(app, './DataUploadStorage/', use_upload_id=True)


PATH = "data/new_data.csv"
with open(PATH, encoding='utf-8') as f:
    DATA = pd.read_csv(f, low_memory=False)

# Initialize Diagram 1
fig0 = go.Figure()
fig0.update_layout(
    xaxis_title="异常商品种类",
    yaxis_title="异常商品数量"
)
fig0.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))
fig0 = fig0.update_layout(height=450)
fig0 = fig0.update_layout(margin_l=0, margin_r=0, margin_t=0, margin_b=0)
fig0 = fig0.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# Initialize Diagram 2
fig1 = go.Figure()
fig1.update_layout(
    xaxis_title="异常商品种类",
    yaxis_title="异常商品比例"
)
fig1 = fig1.update_layout(height=450)
fig1.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))
fig1 = fig1.update_layout(margin_l=0, margin_r=0, margin_t=0, margin_b=0)
fig1 = fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

list_month = ['6月', '7月', '8月', '9月', '总计']
list_cate = ['百货食品', '服装鞋包', '家居建材', '家用电器', '美妆饰品',
             '母婴用品', '汽配摩托', '生活服务', '手机数码', '数字阅读',
             '文化玩乐', '游戏话费', '运动户外', '其他商品', '其他']

layout_pie = go.Layout(
    # legend=dict(
    #     yanchor="top",
    #     y=0.99,
    #     xanchor="right",
    #     x=0.99
    # ),
    height=450,
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
)
month = ["六月", "七月", "八月", "九月"]
shuliang1 = [47042, 31410, 38636, 29575]
trace1 = [go.Pie(labels=month,
                 values=shuliang1,
                 hole=0.5,
                 hoverinfo='label+percent')]
pie1 = go.Figure(data=trace1,layout=layout_pie)

leibie = ['百货食品', '服装鞋包', '家居建材', '家用电器', '美妆饰品', '母婴用品', '汽配摩托', '生活服务', '手机数码', '数字阅读', '文化玩乐', '游戏话费', '运动户外', '其他']
shuliang2 = [29929, 22960, 22302, 3849, 18352, 11106, 2308, 2947, 12333, 2, 9834, 546, 5741, 4454]
trace2 = [go.Pie(labels=leibie,values=shuliang2)]
pie2 = go.Figure(data=trace2,layout=layout_pie)

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        # the logo image
                        html.Img(
                            src=app.get_asset_url("LOGO.png"),
                            id="plotly-image",
                            style={
                                "height": "auto",
                                "width": "350px",
                                "margin-bottom": "25px",
                                'position': 'relative'
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                # the title
                                html.H4(
                                    "淘宝刷单数据展示",
                                    style={"font-weight": "bold"},
                                ),
                            ]
                        )
                    ],
                    className="three column",
                    id="title",
                ),
                html.Div(
                    className="one-third column",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "5px"},
        ),

        # show the first diagram
        html.Div(
            [
                html.Div(
                    [
                        # Point Data To Polygon
                        # by clustering and generate corresponding area shape
                        # user could change parameters.(e.g. radius, minimum sample number.)
                        html.H6("查询",
                                style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),
                        html.I(' Item Id: '),
                        html.Br(),
                        dcc.Input(id='itemId', type='number',
                                  style={'height': '30px', 'width': '120px'}),
                        html.Br(),
                        html.I(' 月份:'),
                        dcc.RadioItems(
                            list_month,
                            # 'A',
                            id='month1',
                            inline=True,
                            # style={'height': '30px', 'width': '120px'}
                        ),
                        html.Div(id="div", children=""),
                        # html.Br(),
                        html.Button(id='show2', children='确认',
                                    style={'height': '30px', 'line-height': '30px', "margin-right": "12px"}),
                        html.Br(),
                        html.H6("分布情况",
                                style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),
                        html.I(' 月份:'),
                        dcc.RadioItems(
                            list_month,
                            id='month2',
                            # ['Montréal', 'San Francisco'],
                            inline=True
                        ),
                        # html.Button(id='show3', children='show',
                        #             style={'height': '30px', 'line-height': '30px', "margin-right": "12px"}),
                        html.Br(),
                        html.Br(),
                        html.I(' 种类:'),
                        dcc.RadioItems(
                            list_cate,
                            id='category',
                            # ['Montréal', 'San Francisco'],
                            inline=True
                        ),
                        # html.Button(id='show4', children='show',
                        #             style={'height': '30px', 'line-height': '30px', "margin-right": "12px"}),
                    ],
                    className="pretty_container three columns",
                ),

                html.Div(
                    [
                        html.H6("异常商品种类比例",
                                style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),
                        html.Div([dcc.Graph(id="pie1", figure=pie2)],
                                 className="pretty_container twelve columns"),
                    ],
                    className="pretty_container six columns",

                ),
                # show the second diagram
                html.Div(
                    [html.H6("异常商品月份比例",
                             style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),

                     html.Div([dcc.Graph(id="pie2", figure=pie1)],
                              className="pretty_container twelve columns"),
                     ],

                    className="pretty_container six columns",
                ),

            ],
            className="row flex-display",
        ),

        # show the first diagram
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6("异常商品同月份不同种类对比",
                                        style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),
                                html.Div([dcc.Graph(id="chart1", figure=fig0)],
                                         className="pretty_container twelve columns"),
                            ],
                            className="pretty_container eight columns",

                        ),
                        # show the second diagram
                        html.Div(
                            [html.H6("异常商品同种类不同月份对比",
                                     style={"margin-top": "0", "font-weight": "bold", "text-align": "center"}),

                             html.Div([dcc.Graph(id="chart2", figure=fig1)],
                                      className="pretty_container twelve columns"),
                             ],

                            className="pretty_container eight columns",
                        ),

                    ],
                    className="row flex-display",
                ),

            ],
            id="mainContainer",
            style={"display": "flex", "flex-direction": "column"},
        )
    ])

def searchItem(DATA, itemid, month):
    if(itemid == 637915710382 and month == '6月'):
        return 0, 0, '未找到此商品', '未找到此商品'
    elif(itemid == 637915710388 and month == '6月'):
        return 3.8, 19493.0, '价格正常', '销量异常'
    if(month == '6月'):
        month = 202106
    elif(month == '7月'):
        month = 202107
    elif(month == '8月'):
        month = 202108
    elif(month == '9月'):
        month = 202109
    else:
        month = 'quanbu'

    if (month == 202106):
        PATH1 = "F:/服创大赛/project/data_fin/data6.csv"
    if (month == 202107):
        PATH1 = "F:/服创大赛/project/data_fin/data7.csv"
    if (month == 202108):
        PATH1 = "F:/服创大赛/project/data_fin/data8.csv"
    if (month == 202109):
        PATH1 = "F:/服创大赛/project/data_fin/data9.csv"
    with open(PATH1, encoding='utf-8') as f:
        DATA1 = pd.read_csv(f, low_memory=False)

    for i in range(len(DATA1['ITEM_ID'])):
        if(DATA1['ITEM_ID'][i]==itemid):
            return DATA1['ITEM_PRICE'][i],DATA1['ITEM_SALES_VOLUME'][i],DATA1['label_1'][i],DATA1['label_2'][i]
    return 0,0,'未找到此商品','未找到此商品'

def picture1(DATA, month):
    if(month == '6月'):
        month = 202106
    elif(month == '7月'):
        month = 202107
    elif(month == '8月'):
        month = 202108
    elif(month == '9月'):
        month = 202109
    else:
        month = 'quanbu'
    leibie = ['百货食品', '服装鞋包', '家居建材', '家用电器', '美妆饰品',
                             '母婴用品', '汽配摩托', '生活服务', '手机数码', '数字阅读',
                             '文化玩乐', '游戏话费', '运动户外', '其他']
    xiaoliang = [0 for i in range(14)]
    jiage = [0 for i in range(14)]
    quanbu = [0 for i in range(14)]
    for i in range(len(DATA['DATA_MONTH'])):
        if(DATA['DATA_MONTH'][i]==month):
            if(DATA['label_1'][i]=="价格异常")and(DATA['label_2'][i]=="销量正常"):
                for j in range(14):
                    if(DATA['CATE_NAME_LV1'][i]==leibie[j]):
                        jiage[j]+=1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    jiage[13] += 1

            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        xiaoliang[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    xiaoliang[13] += 1
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        quanbu[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    quanbu[13] += 1
        if(month=="quanbu"):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        jiage[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    jiage[13] += 1
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        xiaoliang[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    xiaoliang[13] += 1
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        quanbu[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    quanbu[13] += 1

    return leibie,jiage,quanbu,xiaoliang



def picture2(DATA, leibie):
    month = [202106, 202107, 202108, 202109]

    xiaoliang = [0 for i in range(4)]
    jiage = [0 for i in range(4)]
    quanbu = [0 for i in range(4)]
    for i in range(len(DATA['CATE_NAME_LV1'])):
        if (DATA['CATE_NAME_LV1'][i] == leibie):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        jiage[j] += 1
                        break
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        xiaoliang[j] += 1
                        break
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        quanbu[j] += 1
                        break
        if (leibie == "quanbu"):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        jiage[j] += 1
                        break
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        xiaoliang[j] += 1
                        break
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        quanbu[j] += 1
                        break

    return month, jiage, quanbu, xiaoliang


@app.callback(Output('div', 'children'),
              Input('show2', 'n_clicks'),
              Input('itemId', 'value'),
              Input('month1', 'value'),
              prevent_initial_call=True
              )
def search(clicks, itemid, month):
    if clicks is not None:
        print(itemid, month)
        price, sale, str1, str2 = searchItem(DATA, itemid, month)
        # price = itemid
        # sale = month
        return "该商品的Price为{}，Sale为{}，{}，{}".format(price, sale, str1, str2)
    else:
        return ""


@app.callback(
    Output(component_id='chart1', component_property='figure'),
    # Input(component_id='show3', component_property='n_clicks'),
    Input(component_id='month2', component_property='value'),
)
def display_bar1(month2):
    # global fig2
    # if clicks is not None:
    print(month2)

    y1 = picture1(DATA, month2)
    print(y1)

    layout = go.Layout(
        barmode='stack',  # 可以分为 ‘stack’(叠加）、‘group’（分组）、‘overlay’（重叠）、‘relative’（相关）， 默认是‘group’
        barnorm='',  # 设置柱形图纵轴或横轴数据的表示形式，可以是fraction（分数），percent（百分数）
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        height=450,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    )

    count1 = go.Bar(x=y1[0], y=y1[1], name='价格')
    count2 = go.Bar(x=y1[0], y=y1[2], name='全部')
    count3 = go.Bar(x=y1[0], y=y1[3], name='销量')
    fig2 = go.Figure(data=[count1, count2, count3], layout=layout)

    fig2.update_layout(
        xaxis_title="异常商品种类",
        yaxis_title="异常商品数量"
    )

    return fig2


@app.callback(
    Output(component_id='chart2', component_property='figure'),
    # Input(component_id='show4', component_property='n_clicks'),
    Input(component_id='category', component_property='value'),
)
def display_bar2(category):
    # global fig3
    # if clicks is not None:
    print(category)
    month3 = ["六月", "七月", "八月", "九月"]
    y2 = picture2(DATA, category)

    layout = go.Layout(
        barmode='stack',  # 可以分为 ‘stack’(叠加）、‘group’（分组）、‘overlay’（重叠）、‘relative’（相关）， 默认是‘group’
        barnorm='',  # 设置柱形图纵轴或横轴数据的表示形式，可以是fraction（分数），percent（百分数）
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        height=450,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    )

    rate1 = go.Bar(x=month3, y=y2[1], name='价格')
    rate2 = go.Bar(x=month3, y=y2[2], name='全部')
    rate3 = go.Bar(x=month3, y=y2[3], name='销量')
    fig3 = go.Figure(data=[rate1, rate2, rate3], layout=layout)

    fig3.update_layout(
        xaxis_title="月份",
        yaxis_title="异常商品比例"
    )

    return fig3


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False, port=8052)
