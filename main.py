from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def bingo_card():
	b_col = random.sample(range(15), 5)
	b_col.sort()
	i_col = random.sample(range(16, 31), 5)
	i_col.sort()
	n_col = random.sample(range(31, 46), 5)
	n_col.sort()
	g_col = random.sample(range(46, 61), 5)
	g_col.sort()
	o_col = random.sample(range(61, 76), 5)
	o_col.sort()
	return render_template('index.html',
		b1 = b_col[0],
		b2 = b_col[1], 
		b3 = b_col[2],
		b4 = b_col[3], 
		b5 = b_col[4],
		i1 = i_col[1],
		i2 = i_col[2], 
		i3 = i_col[3],
		i4 = i_col[4], 
		i5 = i_col[0],
		n1 = n_col[0],
		n2 = n_col[1], 
		n3 = "FREE",
		n4 = n_col[2], 
		n5 = n_col[3],
		g1 = g_col[0],
		g2 = g_col[1], 
		g3 = g_col[2],
		g4 = g_col[3], 
		g5 = g_col[4],
		o1 = o_col[0],
		o2 = o_col[1], 
		o3 = o_col[2],
		o4 = o_col[3], 
		o5 = o_col[4])




if __name__ == "__main__":
	app.run(debug=True)


