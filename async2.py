from aiohttp import web

async def handle(request):
    return web.Response(text="Hello Gammaedge")


#making a web application that will handle the incoming requests
app=web.Application()

app.router.add_get("",handle)

if __name__=="__main__":
    web.run_app(app)


