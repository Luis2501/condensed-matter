from graphene import graphene_model
from plotly.subplots import make_subplots
import plotly.graph_objects as go

	
graphene = graphene_model()
	
E, kx, ky = graphene.energy()

fig = go.Figure()

# Add surface trace
fig.add_trace(go.Surface(z=E(1), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=400,
    height=500,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add dropdown
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
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
#fig.update_layout(
 #   annotations=[
  #      dict(text="Trace type:", showarrow=False,
                             #x=0, y=1.08, yref="paper", align="left")
   # ]
#)

fig.show()	
