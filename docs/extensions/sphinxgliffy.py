from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

# Class represents the node used to start the <details> tag
class gliffy(nodes.Structural, nodes.Element):
    pass

# Class represents the node used to end the <details> tag
#class finish(nodes.Structural, nodes.Element):
#    pass

# The main class
class Sphinxgliffy(Directive):

    # Gets content from the directive
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    ##'path': directives.unchanged,}
    has_content = False
    
    def run(self):
        
        # Needed to get access to options
        global options
        ##options = self.options
        
        # This is the content of the collapsible
        # nested_parse needed so other directives can be inside the collapsible
        ##par = nodes.paragraph()
        ##self.state.nested_parse(self.content, self.content_offset, par)
        ##reference = directives.uri(self.arguments[0])
        ##self.options['uri'] = reference
        options = self.options
        # Creates the classes to call the other methods
        html_node = gliffy()
        ##html_node += par
        ##html_node += finish()
        
        return [html_node]

# Visit and depart methods come as pairs
# Visit creates the collapsible
# The <details> tag is left open so rst (including directives) can be inserted
def visit_gliffy(self, node):

    # Collapsible is made with <details> tags
    # The title is represented in <summary> tags
    code = """<object data='"""
    code += """_images/test-svg.svg"""
    code += """' type='image/svg+xml'></object>"""
    ##code += options["path"]
    ##code += """' type="image/svg+xml></object>"""
    self.body.append(code)

def depart_gliffy(self, node):
    pass

#def visit_col_html(self, node):
#    pass

# Closes the <details> tag after rst has been inserted
#def depart_col_html(self, node):
#    code = """</details>"""
#    self.body.append(code) 

# Setups up directives and nodes
def setup(app):
    app.add_directive("sphinxgliffy", Sphinxgliffy)
    app.add_node(gliffy, html=(visit_gliffy, depart_gliffy))
    #app.add_node(finish, html=(visit_col_html, depart_col_html))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
