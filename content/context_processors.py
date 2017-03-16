from django.conf import settings

  def currentPath(request):
    return {'current_path': request.get_full_path()}
