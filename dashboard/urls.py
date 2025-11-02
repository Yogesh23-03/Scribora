from django.urls import include, path

from dashboard import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('notes',views.notes, name='notes'),
    path('delete_note/<int:pk>',views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>',views.NotesDetailView, name='notes_detail'),
    path('homework',views.HomeWork, name='homework'),
    path('update_homework/<int:pk>',views.update_homework, name='update_homework'),
    path('update_homework1/<int:pk>',views.update_homework1, name='update_homework1'),
    path('delete_homework/<int:pk>',views.delete_homework, name='delete_homework'),
    path('youtube',views.youtube, name='youtube'),
    path('todo',views.todo, name='todo'),
    path('update_todo/<int:pk>',views.update_todo, name='update_todo'),
    path('update_todo1/<int:pk>',views.update_todo1, name='update_todo1'),
    path('delete_todo/<int:pk>',views.delete_todo, name='delete_todo'),
    path('books',views.books, name='books'),
    path('dictionary',views.dictionary, name='dictionary'),
    path('wikipedia',views.wikipedia_search, name='wikipedia'),
    path('conversion',views.conversion, name='conversion'),
    
]
