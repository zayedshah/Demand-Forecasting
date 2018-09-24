from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connected_components', methods=['POST'])
def connected_components():
	graph = request.get_json()
	
	groups = []
	nodes = set(graph.keys())

	while nodes:
	    node = nodes.pop()
	    group = {node}
	    stack = [node]
	    while stack:
	        node = stack.pop()
	        neighbours = set(graph[node])
	        neighbours.difference_update(group)
	        group.update(neighbours)
	        nodes.difference_update(neighbours)
	        stack.extend(neighbours)
	    groups.append(group)

	return jsonify({'Number of Connected Components':str(len(groups))})

if __name__ == '__main__':
	app.run()