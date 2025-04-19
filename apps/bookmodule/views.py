from django.shortcuts import render
from .models import Book
from django.db.models import Count
from django.db.models import Min
from .models import Department
from .models import Course
from .models import Student

# def index(request):
#     name = request.GET.get("name") or "world!"  #add this line
#     return render(request, "bookmodule/index.html" , {"name": name})  #replace the word “world!” with the variable name
def index2(request, val1 = 0):   #add the view function (index2)
    return render(request, "bookmodule/index2.html", {"val1": val1})
# def viewbook(request, bookId):
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#     context = {'book':targetBook} # book is the variable name accessible by the template
#     return render(request, 'bookmodule/show.html', context)
def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def search_books(request):
    return render(request, 'bookmodule/search.html') 
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        # Retrieve form data
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1') == 'on'  # Check if checkbox is checked
        isAuthor = request.POST.get('option2') == 'on'  # Check if checkbox is checked

        # Get the list of books
        books = __getBooksList()
        filtered_books = []

        # Filter books based on search criteria
        for book in books:
            match = False
            if isTitle and keyword in book['title'].lower():
                match = True
            if not match and isAuthor and keyword in book['author'].lower():
                match = True

            if match:
                filtered_books.append(book)

        # Render the results in a new template
        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  # case-insensitive search
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

from django.shortcuts import render
from .models import Book

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False,
        title__icontains='and',
        edition__gte=2
    ).exclude(price__lte=100)[:10]
    
    if mybooks:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')



def task1(request):
    departments = Department.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/task1.html', {'departments': departments})
def task1(request):
    departments = Department.objects.annotate(student_count=Count('students'))  
    return render(request, 'bookmodule/task1.html', {'departments': departments})  # fixed variable name

def task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task2.html', {'courses': courses})

def task3(request):

    dept = Department.objects.annotate(
        oldest_student_id=Min('students__id')
    ).filter(
        oldest_student_id__isnull=False
    ).values('name', 'oldest_student_id')

    oldest_student_ids = [dept['oldest_student_id'] for dept in dept]
    oldest_students = Student.objects.in_bulk(oldest_student_ids, field_name='id')

    oldest_per_dept = [
        (dept['name'], oldest_students[dept['oldest_student_id']].name)
        for dept in dept
    ]

    return render(request, 'bookmodule/task3.html', {'data': oldest_per_dept})
    
 
def task4(request):
    departments = Department.objects.annotate(student_count=Count('students')) \
                                    .filter(student_count__gt=2) \
                                    .order_by('student_count')
    return render(request, 'bookmodule/task4.html', {'departments': departments})
