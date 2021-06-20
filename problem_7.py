from collections import defaultdict
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.children = defaultdict(RouteTrie)
        self.handler = None

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self
        if len(path) == 0:
            return current.handler
        for node in path:
            #print(node, path)
            if node == '' and len(path) == 2:
                break
            if node in current.children:
                current = current.children[node]
            else:
                return None
        return current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, route_handler):
        self.root = RouteTrie()
        self.root.handler = route_handler

    def insert(self, nodes, handler):
        # Insert the node as before
        current = self.root
        for node in nodes:
            current = current.children[node]
        current.handler = handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler=None, error_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrieNode(root_handler)
        self.error_handler = error_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        k = self.split_path(path)
        self.root.insert(k, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        k = self.split_path(path)
        h = self.root.root.find(k)
        if h is None:
            return self.error_handler
        return h

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        k = path.split('/')
        if k[0] == '':
            k = k[1:]
        if k[len(k)-1] == '':
            k = k[:-1]
        return k


# create the router and add a route
router = Router("root handler","not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "me handler")  # add a route
router.add_handler("/home/about/linux", "linux handler")  # add a route
router.add_handler("/home/about/windows10", "windows10 handler")  # add a route




# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'me handler'
print(router.lookup("/home/about/linux"))  # should print 'linux handler'