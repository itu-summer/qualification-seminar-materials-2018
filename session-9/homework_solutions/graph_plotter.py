import os
import random
import webbrowser
from jinja2 import Template


template_str = '''
<!DOCTYPE html>
<html><head>
  <title>{{title}}</title>

  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" type="text/css">

  <style type="text/css">
    #mynetwork {
      width: 1400px;
      height: 800px;
      border: 1px solid lightgray;
    }

    p {
      max-width:700px;
    }
  </style>
<style></style></head>
<body>

<div id="mynetwork"><div class="vis-network" tabindex="900" style="position: relative; overflow: hidden; -webkit-user-select: none; -webkit-user-drag: none; width: 100%; height: 100%;"><canvas width="1200" height="800" style="position: relative; -webkit-user-select: none; -webkit-user-drag: none; width: 100%; height: 100%;"></canvas></div></div>

<script type="text/javascript">
  // create an array with nodes
  var nodes = new vis.DataSet([
    {% for n, idx in nodes.items() %}{ id: {{ idx }}, label: "{{ n }}", color: 'rgba({{node_colors[n]}})'},
    {% endfor %}
  ]);
  // create an array with edges
  var edges = new vis.DataSet([
    {% for r in rels %}{ from: {{ r[0] }},to: {{ r[1] }}, {% if directed %} arrows:'to', {% endif %}},
    {% endfor %}
  ]);

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
    nodes: {borderWidth: 2},
    edges: {
      arrows: {
        to: {
          scaleFactor: 0.5
        }
      }
    },
    interaction: {hover: true}
  }
  var network = new vis.Network(container, data, options);
</script>

</body></html>
'''


def _color_nodes(nodes):
    unique_colors = {}
    for node in nodes:
        rgb = [str(random.randint(0, 255)) for _ in range(3)]
        rgba = rgb + ['0.5']
        unique_colors[node] = ','.join(rgba)
    return unique_colors


def _colors_from_nodes(graph, nodes):
    unique_colors = {}
    for node in nodes:
        vertex = graph.vertices[node]
        if vertex.get_color() == 'white':
            rgb = ['240', '240', '240']
        elif vertex.get_color() == 'gray':
            rgb = ['200', '200', '200']
        elif vertex.get_color() == 'black':
            rgb = ['30', '30', '30']
        else:
            rgb = [str(random.randint(0, 255)) for _ in range(3)]
        rgba = rgb + ['0.7']
        unique_colors[node] = ','.join(rgba)
    return unique_colors


def make_plot(graph, directed=True, w_node_color=False,
              graph_file='tmp_graph.html'):
    nodes = {name: idx for idx, name in enumerate(graph.vertices.keys())}
    relations = graph.get_edges()
    relations_idx = [(nodes[s], nodes[t]) for s, t in relations]

    template = Template(template_str)
    if w_node_color:
        # nodes = {name: idx for idx, name in enumerate(graph.vertices.keys())}
        colors = _colors_from_nodes(graph, nodes.keys())
    else:
        colors = _color_nodes(nodes.keys())
    visJS = template.render(nodes=nodes, rels=relations_idx,
                            node_colors=colors,
                            title='My graph', directed=directed)

    with open(graph_file, 'w') as f:
        f.write(visJS)
    webbrowser.open('file://' + os.path.realpath(graph_file))
