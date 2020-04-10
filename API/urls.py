from controller import app, index
from user import urls

app.add_api_route('/', index)

# user
for (methods, path, func, model) in urls.path_list:
    app.add_api_route(path=f'/user/{path}', endpoint=func, response_model=model, methods=methods)
