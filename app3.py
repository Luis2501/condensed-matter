from graphene import graphene_model
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

graphene = graphene_model()
E, kx, ky = graphene.energy()

K = (2*np.pi/3, (2*np.pi)/(3*np.sqrt(3)))
KP = (2*np.pi/3, -(2*np.pi)/(3*np.sqrt(3)))
			
x = [K[0], 0, -K[0], -KP[0], 0, KP[0], K[0]]  
y = [K[1], 2*K[1], K[1], KP[1], 2*KP[1], KP[1], K[1]]
z = -2*np.ones(len(x))

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, visible=True))
fig.add_trace(go.Surface(x= kx, y=ky, z=E(1), colorscale="Viridis", visible=True, showscale=False))
fig.add_trace(go.Surface(x =kx, y=ky, z=E(-1), colorscale="Viridis", visible=True, showscale=False))

fig.add_trace(go.Heatmap(x= kx, y=ky, z=E(1), colorscale='Viridis', visible = False, showscale=False))
fig.add_trace(go.Heatmap(x= kx, y=ky, z=E(-1), colorscale='Viridis', visible = False, showscale=False))

# Update plot sizing
fig.update_layout(
    width=500,
    height=600,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

"""
# Add buttons that add shapes
cluster0 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x0), y1=max(y0),
                            line=dict(color="DarkOrange"))]
cluster1 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x1), y0=min(y1),
                            x1=max(x1), y1=max(y1),
                            line=dict(color="Crimson"))]
cluster2 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x2), y0=min(y2),
                            x1=max(x2), y1=max(y2),
                            line=dict(color="RebeccaPurple"))]
"""

fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(label="3D Surface",
                     method="restyle",
                     args=[{"visible": [True, True, True, False, False]}, 
                     	   {"type": "surface"}]),
                dict(label="π*-band",
                     method="restyle",
                     args=[{"visible": [False, False, False, True, False]}, 
                           {"type": "heatmap"}]),
                dict(label="π-band",
                     method="update",
                     args=[{"visible": [False, False, False, False, True]},
                     	   {"type": "heatmap"}]),
            ],
        )
    ]
)


# Update remaining layout properties
fig.update_layout(
    title_text="Band structure of graphene",
    showlegend=False,
)

fig.show()
