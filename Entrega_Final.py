from dash import Dash, html, dcc
import plotly.express as px
import psycopg2

# Conectar a la base de datos
try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='PROYECTO',
        port='5432'
    )

    cursor = connection.cursor()

    # Consultas
    cursor.execute("SELECT empleado.nombre, count(*) as num_publicacion from registro_publicacion inner join empleado on empleado.cedula = cedula_empleado group by empleado.nombre")
    rows = cursor.fetchall()
    fig1 = px.bar(rows, x=0, y=1, color_discrete_sequence=["#800080"], title="Empleados con Mejor Rendimiento")

    cursor.execute("SELECT ciudad, count(*) as num_clientes from cliente group by ciudad")
    rows2 = cursor.fetchall()
    fig2 = px.line(rows2, x=0, y=1, color_discrete_sequence=["#800080"], title="Ciudades con Más Ventas")

    cursor.execute("SELECT nombre_producto, count(*) as num_productos, rank() over(order by count(*) desc) from registro_compra group by nombre_producto")
    rows3 = cursor.fetchall()
    fig3 = px.scatter(rows3, x=0, y=1, color_discrete_sequence=["#800080"], title="Productos Más Vendidos")

    cursor.execute("SELECT nombre_producto, count(*) as num_productos, rank() over(order by count(*) desc) from registro_compra WHERE nombre_producto like 'F%' group by nombre_producto")
    rows4 = cursor.fetchall()
    fig4 = px.scatter(rows4, x=0, y=1, color_discrete_sequence=["#800080"], title="Productos que Empiezan con 'F'")

    cursor.execute("select nombre, precio, rank() over(order by precio) from producto")
    rows5 = cursor.fetchall()
    fig5 = px.bar(rows5, x=0, y=1, color_discrete_sequence=["#800080"], title="Rango de Precios de Productos")

    cursor.execute("select nombre, precio, rank() over(order by precio) from producto where precio > 125000")
    rows6 = cursor.fetchall()
    fig6 = px.bar(rows6, x=0, y=1, color_discrete_sequence=["#800080"], title="Productos con Precio Mayor a 125k")

    cursor.execute("SELECT transportadora, COUNT(*) AS uso_transportadora FROM registro_envio GROUP BY transportadora")
    rows7 = cursor.fetchall()
    data = [{'transportadora': row[0], 'uso_transportadora': row[1]} for row in rows7]
    fig7 = px.pie(data, names='transportadora', values='uso_transportadora', color_discrete_sequence=["#800080"], title="Preferencia de Transportadoras")

    # Crear la aplicación Dash
    app = Dash(__name__)

    # Estilos CSS personalizados
    app.layout = html.Div(style={
        'fontFamily': 'Arial, sans-serif',
        'backgroundColor': '#f0f0f5',
        'padding': '20px'
    }, children=[
        # Encabezado
        html.Div(style={
            'textAlign': 'center',
            'backgroundColor': '#4B0082',
            'color': 'white',
            'padding': '30px',
            'borderRadius': '15px',
            'boxShadow': '0 6px 12px rgba(0, 0, 0, 0.15)',
            'marginBottom': '30px'
        }, children=[
            html.H1('Análisis de Datos', style={'fontSize': '42px', 'margin': '0'}),
            html.P('SD grupo empresarial', style={'fontSize': '22px', 'margin': '0'}),
        ]),

        # Cuerpo de la página
        html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around', 'marginTop': '30px'}, children=[

            # Tarjeta para Empleados con Mejor Rendimiento
            html.Div(style={
                'backgroundColor': 'white',
                'borderRadius': '15px',
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
                'width': '45%',
                'transition': 'transform 0.2s',
                ':hover': {
                    'transform': 'scale(1.05)'
                }
            }, children=[
                html.H3("Empleados con Mejor Rendimiento", style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph1', figure=fig1),
                html.Div(
                    children='Es evidente que Silvia Daniela Lotero Ruiz destaca en cuanto a rendimiento, ya que logró más de 700 ventas durante el período analizado, superando significativamente a sus compañeros en términos de desempeño.',
                    style={'marginTop': '10px', 'padding': '15px', 'backgroundColor': '#e6e6fa', 'border': '1px solid #ddd', 'borderRadius': '10px'}
                )
            ]),

            # Tarjeta para Ciudades con Más Ventas
            html.Div(style={
                'backgroundColor': 'white',
                'borderRadius': '15px',
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
                'width': '45%',
                'transition': 'transform 0.2s',
                ':hover': {
                    'transform': 'scale(1.05)'
                }
            }, children=[
                html.H3("Ciudades con Más Ventas", style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph2', figure=fig2),
                html.Div(
                    children='Para garantizar un análisis exhaustivo, consideramos las localidades de Bogotá como ciudades debido a su alta demanda. Al analizar los datos, se destaca que Suba es la localidad con el mayor número de registros de venta, consolidándose como la principal ''ciudad'' en este contexto local. ',
                    style={'marginTop': '10px', 'padding': '15px', 'backgroundColor': '#e6e6fa', 'border': '1px solid #ddd', 'borderRadius': '10px'}
                )
            ]),

            # Tarjeta para Productos Más Vendidos
            html.Div(style={
                'backgroundColor': 'white',
                'borderRadius': '15px',
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
                'width': '45%',
                'transition': 'transform 0.2s',
                ':hover': {
                    'transform': 'scale(1.05)'
                }
            }, children=[
                html.H3("Productos Más Vendidos", style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph3', figure=fig3),
                dcc.Graph(id='graph4', figure=fig4),
                html.Div(
                    children='Se nota que la cantidad de productos más vendidos oscila entre 4 y 3 unidades, lo que resulta en un análisis intrigante, dado que no se encontraron productos repetidos más de dos veces o que superaran las 4 unidades vendidas. Y como prueba buscamos entre los más comprados, aquellos que empezaran por la letra ''F'' y como podemos ver, estan entre 4 y 3 unidades.',
                    style={'marginTop': '10px', 'padding': '15px', 'backgroundColor': '#e6e6fa', 'border': '1px solid #ddd', 'borderRadius': '10px'}
                )
            ]),

            # Tarjeta para Rango de Precios de Productos
            html.Div(style={
                'backgroundColor': 'white',
                'borderRadius': '15px',
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
                'width': '45%',
                'transition': 'transform 0.2s',
                ':hover': {
                    'transform': 'scale(1.05)'
                }
            }, children=[
                html.H3("Rango de Precios de Productos", style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph5', figure=fig5),
                html.P('Rango para productos cuyo precio es más de 125k', style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph6', figure=fig6),
                html.Div(
                    children='La gráfica puede parecer abrumadora debido a la gran cantidad de productos representados, lo que puede afectar su visualización. Sin embargo, en la esquina inferior derecha, se puede apreciar de manera más clara el crecimiento exponencial de los precios. Se observa un rango de precios entre un mínimo de $3.000 y un máximo de $1´700.000, todo en pesos Colombianos',
                    style={'marginTop': '10px', 'padding': '15px', 'backgroundColor': '#e6e6fa', 'border': '1px solid #ddd', 'borderRadius': '10px'}
                )
            ]),

            # Tarjeta para Preferencia de Transportadoras
            html.Div(style={
                'backgroundColor': 'white',
                'borderRadius': '15px',
                'padding': '20px',
                'margin': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.1)',
                'width': '45%',
                'transition': 'transform 0.2s',
                ':hover': {
                    'transform': 'scale(1.05)'
                }
            }, children=[
                html.H3("Preferencia de Transportadoras", style={'color': '#4B0082', 'textAlign': 'center'}),
                dcc.Graph(id='graph7', figure=fig7),
                html.Div(
                    children='Se destaca la preferencia por ''MELI Logistics'', evidenciando la confianza y familiaridad de los usuarios con la seguridad y eficiencia que ofrece esta empresa de transporte. Ha emergido como la opción más confiable en nuestro ámbito empresarial, aunque no se menosprecia el excelente trabajo realizado por otras empresas de transporte que igualmente ofrecen un servicio impecable.',
                    style={'marginTop': '10px', 'padding': '15px', 'backgroundColor': '#e6e6fa', 'border': '1px solid #ddd', 'borderRadius': '10px'}
                )
            ]),
        ]),

        # Pie de página
        html.Footer(style={
            'textAlign': 'center',
            'padding': '20px',
            'marginTop': '30px',
            'borderTop': '1px solid #ddd',
            'color': '#4B0082'
        }, children=[
            html.P('© 2024 SD Grupo Empresarial. Todos los derechos reservados.')
        ])
    ])

    # Ejecutar la aplicación
    if __name__ == '__main__':
        app.run_server(debug=False)

except Exception as ex:
    print(ex)

finally:
    connection.close()
    print("Conexión finalizada")

