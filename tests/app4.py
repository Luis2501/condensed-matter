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
#fig.add_trace(go.Scatter3d(x=x, y=y, z=z, visible=True))
#fig.add_trace(go.Surface(x= kx, y=ky, z=E(1), colorscale="Viridis", visible=True, showscale=False))
#fig.add_trace(go.Surface(x =kx, y=ky, z=E(-1), colorscale="Viridis", visible=True, showscale=False))

#fig.add_trace(go.Heatmap(x= kx, y=ky, z=E(1), colorscale='Viridis', visible = False, showscale=False))
#fig.add_trace(go.Heatmap(x= kx, y=ky, z=E(-1), colorscale='Viridis', visible = False, showscale=False))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

hopping_integral = np.round_(np.arange(-3, 0, 0.1),2)

# Add traces, one for each slider step
for t in hopping_integral:
            
	fig.add_trace(go.Surface(x= kx, y=ky, z=E(1, t), name="t=" + str(t), colorscale="Viridis", visible=False))
	fig.add_trace(go.Surface(x =kx, y=ky, z=E(-1, t), name="t=" + str(t), colorscale="Viridis", visible=False))

print(fig.data[10].name, fig.data[11].name)

# Make 10th trace visible
fig.data[10].visible = True
fig.data[11].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i:i+1] = [True for i in range(2)]   # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "t: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

# Update remaining layout properties
fig.update_layout(
    title_text="Band structure of graphene",
    showlegend=False,
)

fig.show()
