def app_clicks(get_response):
    def middleware(request):
        clicks_count = request.session.get('clicks_count', 0)
        clicks_count += 1
        request.session['clicks_count'] = clicks_count
        request.clicks_count = clicks_count
        return get_response(request)
    return middleware

def last_viewed_photos(get_response):
    def middleware(request):
        request.last_viewed_pet_photos = request.session['last_viewed_pet_photos']
        return get_response(request)
    return middleware