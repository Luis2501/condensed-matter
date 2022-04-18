from graphene import graphene_model
import plotly.graph_objects as go
import numpy as np

p = 1

# load dataset
graphene = graphene_model()
E, kx, ky = graphene.energy()	

K = (2*np.pi/3, (2*np.pi)/(3*np.sqrt(3)))
KP = (2*np.pi/3, -(2*np.pi)/(3*np.sqrt(3)))
			
x = [K[0], 0, -K[0], -KP[0], 0, KP[0], K[0]]  
y = [K[1], 2*K[1], K[1], KP[1], 2*KP[1], KP[1], K[1]]

# Create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Surface(z=E(1), colorscale="Viridis", showscale=False))
#fig.add_trace(go.Surface(z=E(-1), colorscale="Viridis", showscale=False))

# Update plot sizing
fig.update_layout(
    width=p*800,
    height=p*900,
    autosize=False,
    margin=dict(t=p*100, b=0, l=0, r=0),
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=p*1, y=p*1, z=p*0.7),
    aspectmode="manual"
)

# Add drowdowns
# button_layer_1_height = 1.08
button_layer_1_height = p*1.12
button_layer_2_height = p*1.065

fig.update_layout(
    updatemenus=[
    	dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label="3D Surface",
                    method="restyle"
                ),
                dict(
                    args=["type", "heatmap"],
                    label="Heatmap",
                    method="restyle"
                )
            ]),
            pad={"r": p*10, "t": p*10},
            showactive=True,
            x=p*0.55,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=["colorscale", "Viridis"],
                    label="Viridis", #π
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Cividis"],
                    label="Cividis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Blues"],
                    label="Blues",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Greens"],
                    label="Greens",
                    method="restyle"
                ),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": p*10, "t": p*10},
            showactive=True,
            x=p*0.1,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=["reversescale", False],
                    label="False",
                    method="restyle"
                ),
                dict(
                    args=["reversescale", True],
                    label="True",
                    method="restyle"
                )
            ]),
            type = "buttons",
            direction="right",
            pad={"r": p*10, "t": p*10},
            showactive=True,
            x=p*0.13,
            xanchor="left",
            y=button_layer_2_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=[{"contours.showlines": False, "type": "contour"}],
                    label="Hide lines",
                    method="restyle"
                ),
                dict(
                    args=[{"contours.showlines": True, "type": "contour"}],
                    label="Show lines",
                    method="restyle"
                ),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": p*10, "t": p*10},
            showactive=True,
            x=p*0.5,
            xanchor="left",
            y=button_layer_2_height,
            yanchor="top"
        ),
    ]
)

fig.update_layout( #title={
        #'text': "Band structure of graphene",
        #'y':0,
        #'x':0}, 
    annotations=[
    	dict(text="Trace type:", showarrow=False,
                             x=p*0.5, xref="paper", y=p*1.1, yref="paper"),
        dict(text="Colorscale:", x=p*0, xref="paper", y=p*1.1, yref="paper",
                             align="left", showarrow=False),
        dict(text="Reverse<br>Colorscale:", x=p*0, xref="paper", y=p*1.06,
                             yref="paper", showarrow=False),
        dict(text="Lines:", x=p*0.47, xref="paper", y=p*1.045, yref="paper",
                             showarrow=False)
    ])

fig.write_html("Band_structure_of_graphene.html")
fig.show()
