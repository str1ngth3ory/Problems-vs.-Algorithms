# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, notfoundhandler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler, notfoundhandler)

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.root

        for path_part in path_parts:
            if path_part not in curr.children:
                curr.insert(path_part)
            curr = curr.children[path_part]

        curr.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root

        if path_parts == ['']:
            return curr.handler

        for path_part in path_parts:
            if path_part not in curr.children:
                return self.root.notfoundhandler
            curr = curr.children[path_part]
        if curr.handler:
            return curr.handler
        else:
            return curr.notfoundhandler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None, notfoundhandler='not found handler'):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = handler
        self.notfoundhandler = notfoundhandler

    def insert(self, pathpart):
        # Insert the node as before
        self.children[pathpart] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, notfoundhandler = '404 page not found'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler, notfoundhandler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.root.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '':
            return 'No path was specified.'

        path_parts = self.split_path(path)
        return self.root.find(path_parts)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
#         path_parts = []
        if path[-1] == '/':
            return path[:-1].split('/')[1:]
        else:
            return path.split('/')[1:]

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Edge case - empty input, should print 'No path was specified.'
print(router.lookup(""))
