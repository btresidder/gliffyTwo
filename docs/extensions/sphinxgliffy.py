from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

options = [] # Stores URIs
index = 0    # Counter for URI list

# Class represents the node used to insert the svg
class gliffy(nodes.Structural, nodes.Element):
    pass

# The main class
class Sphinxgliffy(Directive):

    # Gets content from the directive
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = False
    
    def run(self):
        
        # Needed to get access to options
        global options

        # Reference is the link to the svg file
        # Adds reference to the options list
        reference = directives.uri(self.arguments[0])
        self.options['uri'] = reference
        options.append(self.options['uri'])
        
        # Creates the svg class
        html_node = None
        html_node = gliffy()
        
        # Adds html class "gliffy_img" to all nodes created from now on
        self.options['classes'] = ['gliffy_img']
        
        # Creates an img version of the svg
        # Necessary to pass X Frame Options denial
        # Image is not visible in browser, hidden by gliffy_img class
        #html_node += nodes.image(rawsource=self.block_text, **self.options)
        html_node += nodes.image(rawsource=self.options['uri'], **self.options)
        
        return [html_node]

# Visit and depart methods come as pairs
# Visit method inserts the svg
def visit_gliffy(self, node):

    global index

    # Adds the svg to an <object>
    code = """<object data='_"""
    if index == 0:
        code += "images/fourth-svg.svg"
    else:
        code += options[index]
        
    code += """' type='image/svg+xml'></object>"""
    index += 1
    
    # Adds the <object>
    self.body.append(code)

def depart_gliffy(self, node):
    pass

# Setups up directives and nodes
def setup(app):
    app.add_directive("sphinxgliffy", Sphinxgliffy)
    app.add_node(gliffy, html=(visit_gliffy, depart_gliffy))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
