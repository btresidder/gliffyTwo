from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

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
        options = None

        # Reference is the link to the svg file
        # Adds reference to the options list
        reference = directives.uri(self.arguments[0])
        self.options['uri'] = reference
        options = self.options
        print("options: ")
        print(options)
        # Creates the svg class
        html_node = None
        #html_node = gliffy()
        
        # Adds html class "gliffy_img" to all nodes created from now on
        self.options['classes'] = ['gliffy_img']
        
        # Creates an img version of the svg
        # Necessary to pass X Frame Options denial
        # Image is not visible in browser, hidden by gliffy_img class
        html_node += nodes.image(rawsource=self.block_text, **self.options)
        self.add_name(html_node)
        print("html_none: ")
        print(html_node)
        return [html_node]

# Visit and depart methods come as pairs
# Visit method inserts the svg
def visit_gliffy(self, node):

    # Adds the svg as an <object>
    code = """<object data='_"""
    code += options['uri']
    code += """' type='image/svg+xml'></object>"""
    
    # Adds the <object> to the 
    self.body.append(code)

def depart_gliffy(self, node):
    options = None

# Setups up directives and nodes
def setup(app):
    app.add_directive("sphinxgliffy", Sphinxgliffy)
    #app.add_node(gliffy, html=(visit_gliffy, depart_gliffy))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
