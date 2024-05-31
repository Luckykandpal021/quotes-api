from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def kotlinQuiz(request):
    quiz_questions = [
    {"id": 1, "question": "What is Kotlin?", "options": ["A programming language", "A dessert", "A city in Japan", "A car brand"], "answer": "A programming language"},
    {"id": 2, "question": "Which company developed Kotlin?", "options": ["Google", "JetBrains", "Apple", "Microsoft"], "answer": "JetBrains"},
    {"id": 3, "question": "What is Kotlin interoperable with?", "options": ["Java", "C++", "Python", "Swift"], "answer": "Java"},
    {"id": 4, "question": "What is the primary IDE for developing Kotlin?", "options": ["Eclipse", "Visual Studio Code", "Xcode", "IntelliJ IDEA"], "answer": "IntelliJ IDEA"},
    {"id": 5, "question": "What is a nullable type in Kotlin?", "options": ["A type that cannot hold null values", "A type that can hold null values", "A type for numbers", "A type for strings"], "answer": "A type that can hold null values"},
    {"id": 6, "question": "What is a data class in Kotlin?", "options": ["A class for storing data", "A class that cannot be modified", "A class with only methods", "A class with no attributes"], "answer": "A class for storing data"},
    {"id": 7, "question": "What is the default visibility modifier in Kotlin?", "options": ["public", "private", "protected", "internal"], "answer": "public"},
    {"id": 8, "question": "What is the keyword used to declare a variable in Kotlin?", "options": ["var", "let", "const", "val"], "answer": "val"},
    {"id": 9, "question": "What is the purpose of `lateinit` in Kotlin?", "options": ["To initialize a variable immediately", "To declare a variable that can be reassigned", "To postpone variable initialization", "To declare a constant"], "answer": "To postpone variable initialization"},
    {"id": 10, "question": "What does `!!` mean in Kotlin?", "options": ["Logical NOT operator", "Safe call operator", "Type cast operator", "Not-null assertion operator"], "answer": "Not-null assertion operator"},
    {"id": 11, "question": "What is the syntax for defining a function in Kotlin?", "options": ["func", "def", "fun", "funct"], "answer": "fun"},
    {"id": 12, "question": "What is the purpose of the `when` keyword in Kotlin?", "options": ["To create a loop", "To declare a variable", "To define a switch-like statement", "To define a class"], "answer": "To define a switch-like statement"},
    {"id": 13, "question": "What is the purpose of the `apply` function in Kotlin?", "options": ["To apply a function to every element in a collection", "To apply a function to an object and return it", "To apply a function to a nullable type", "To apply a function to a string"], "answer": "To apply a function to an object and return it"},
    {"id": 14, "question": "What is the keyword used to define a class in Kotlin?", "options": ["class", "Class", "struct", "object"], "answer": "class"},
    {"id": 15, "question": "What is the purpose of `Coroutine` in Kotlin?", "options": ["To handle exceptions", "To handle asynchronous programming", "To handle data serialization", "To handle user input"], "answer": "To handle asynchronous programming"},
    {"id": 16, "question": "What is the operator used for string interpolation in Kotlin?", "options": ["$", "%", "#", "{}"], "answer": "{}"},
    {"id": 17, "question": "What is the purpose of `inline` functions in Kotlin?", "options": ["To execute a function asynchronously", "To improve performance by reducing function call overhead", "To declare a function without a body", "To hide the implementation details of a function"], "answer": "To improve performance by reducing function call overhead"},
    {"id": 18, "question": "What is the purpose of the `object` keyword in Kotlin?", "options": ["To create an instance of a class", "To declare a class as a singleton", "To declare an abstract class", "To declare an interface"], "answer": "To declare a class as a singleton"},
    {"id": 19, "question": "What is the purpose of the `sealed` keyword in Kotlin?", "options": ["To prevent inheritance", "To allow multiple inheritance", "To define a data structure", "To define a package"], "answer": "To prevent inheritance"},
    {"id": 20, "question": "What is the purpose of the `suspend` keyword in Kotlin?", "options": ["To pause the execution of a function", "To specify that a function can be executed concurrently", "To specify that a function can be executed only once", "To specify that a function can be executed lazily"], "answer": "To specify that a function can be executed concurrently"}
]

    return Response(quiz_questions,status=status.HTTP_200_OK)