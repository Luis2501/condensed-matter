from graphene import graphene_model
from plotly.subplots import make_subplots
import plotly.graph_objects as go
	
fig = make_subplots(rows=2, cols=2, 
		    specs=[[{'type': 'scatter'}, {'type': 'scatter'}],
			   [{'type': 'surface'}, {'type': 'contour'}]])
	
graphene = graphene_model()
R1, R2 = graphene.lattice(1)
K = graphene.reciprocal_lattice(1)
	
kx, ky = graphene.brillouin_zone()
	
fig.add_trace(go.Scatter(x=kx, y=ky, name="Brillouin zone", fill="toself"), row=1, col=2)
fig.add_trace(go.Scatter(x=K[:,0], y=K[:,1], mode="markers", 
			   name="RR", marker=dict(size=20)), row=1, col=2)
	
del kx, ky
	
E, kx, ky = graphene.energy()
	
fig.add_trace(go.Scatter(x=R1[:,0], y=R1[:,1], mode="markers", 
		           name="RD: \"A\"", marker=dict(size=20)), row=1, col=1)

fig.add_trace(go.Scatter(x=R2[:,0], y=R2[:,1], mode="markers", 
			name="RD: \"B\"", marker=dict(color="orange", size=20)), row=1, col=1)
				 
b1, b2 = graphene.b_1, graphene.b_2
	
#Energy
fig.add_trace(go.Surface(x = kx, y=ky, z=0.49*E(1)), row=2, col=1) 
fig.add_trace(go.Surface(x = kx, y=ky, z=0.49*E(-1)), row=2, col=1)
	
fig.add_trace(go.Contour(z= 0.49*E(-1), x=kx, y=ky), row=2, col=2)
	
fig.update_layout(title_text="Electronic propierties of graphene")
fig.show()	
