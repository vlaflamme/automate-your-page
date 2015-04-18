# generate HTML code.

def start_lesson(lesson_title):
    start_lesson_html = '''
<div class="lesson">
    <h1>''' + lesson_title + '''</h1>'''
    return start_lesson_html

def end_lesson():
	end_lesson_html = '''
</div>'''
	return end_lesson_html
  
def start_sub_topic(sub_topic_title):
	start_sub_topic_html = '''
	<div class="sub-topic">
		<h2>''' + sub_topic_title + '''</h2>'''
	return start_sub_topic_html

def end_sub_topic():
	end_sub_topic_html = '''
	</div>'''
	return end_sub_topic_html

#this procedure will be used when Stage 0 and Stage 1 notes are added to the code
def start_det_topic(det_topic_title):
	    start_det_topic_html = '''
		<div class="det-topic">
		    <h3>''' + sub_topic_title + '''</h3>'''
	#return start_det_topic_html

#this procedure will be used when Stage 0 and Stage 1 notes are added to the code
def end_det_topic(det_topic_title):
	    end_det_topic_html = '''
		</div>'''
	#return end_det_topic_html

def start_list():
	start_list_html = '''
			<ul>'''
	return start_list_html

def end_list():
	end_list_html = '''
			</ul>'''
	return end_list_html

def list_item(list_item_text):
	list_item_html = '''
				<li>''' + list_item_text + '''</li>'''
	return list_item_html

def HTML_for_lists(list_of_items):
    HTML_list = ""
    for item in list_of_items:
        HTML_list = HTML_list + list_item(item)
    return HTML_list

top_of_page_html = '''<!--intro to programming notes-->
<!DOCTYPE html>
<html>

<head>
  <link href="Nano-Intro-Pgm-Notes-CSS-Sublime.css" type="text/css" rel="stylesheet" />
  <title>Intro To Web Programming Notes</title>
  <meta charset="UTF-8">
</head>

<body>

  <div class="top-page"><!-- start of testing with images and flex -->
    <div>
      <img src="Images/badlands.jpg" class="images" alt="Badlands National Park Late Afternoon" title="Badlands at Dusk" />
    </div>
    
    <div>
      <p>This page is developed by Virginia LaFlamme<br /><br /> Photography by Virginia LaFlamme</p>
    </div>
  </div>'''

print top_of_page_html
print start_lesson('Stage 2')

print start_sub_topic('Python - Understanding Programming'),start_list(), HTML_for_lists(['A computer is a machine that can execute a program; a computer can do any mechanical computation you can imagine, with the right program',
        'A program describes a very precise sequence of steps / instructions; these steps must be given in a way the computer can execute (mechanically, or without thought).',
        'Computer Science is about how to solve problems by breaking them into smaller pieces; and then precisely and mechanically describing them as a sequence of steps that you can use to solve each piece. Those steps can be executed by a computer.',
        'Programming languages tell a computer what to do; Python is a programming language.',
        'Python Interpreter is a program running on the computer which we will input our Python program into. The interpreter reads the program and executes it according to the rules of the Python language.',
        'Thinking of a Python program, the Python Interpreter, and a web browser as different types of computer programs demonstrates &#34;abstract thinking&#34;',
        'Computer languages are needed to ensure no ambiguity exists in how instructions (code) will be executed by the computer. Programming languages only need a few lines of precise code to tell the computer how to do complex things.',
        'Programming languages include &#34;grammar&#34;, which is the syntax / rules for the code - what is &#34;correct&#34; and what is &#34;not correct&#34;. The code must match the language grammar exactly, otherwise the interpreter will produce a syntax error.',
        'Python expressions are something that has a value - they are legal Python statements; there are rules or &#34;syntax&#34; for how to create expressions.']),end_list(),end_sub_topic()

print start_sub_topic('Python - Coding'),start_list(), HTML_for_lists(['You need to develop a system for finding and fixing &#34;bugs&#34; in your code',
		'A variable is a name that refers to a value. Python allows any sequence of letters and numbers and underscores in a variable name, but does not allow a variable name to start with a number',
        'New variable are introduced using an assignment statement (Name = Expression). After executing the assignment expression, the variable name will refer to the value of the expression on the right side of the assignment',
        'Variable values can change (vary) - when a variable is used, it always refers to the last value assigned to that variable',
        'The equal sign in math means equality; in programming, the equal sign means the value the right side evaluates to is being assigned to the variable name of the left side',
        'Variables are useful because they improve code readability by assigning names that make sense to humans; give a way to store important data; and give a way to change the value of something',
        'A string is a sequence of characters surrounded by quotes (either single or double) - a string is required to start and end with the same type of quote (so it is possible to include quotes as part of the text contained in the string',
        'Strings are needed to assign text (not numbers) to a variable, so Python sees the quotes and treats everything inside of the quotes as the value to assign to the variable.',
        'You can concatenate strings by using the plus sign, e.g. print "Hello" + name + "!". You can also multiply, so the code will show that many instances of the string being multiplied',
        'Indexing strings - this allows you to select (extract) sub-sequences from a string; you indicate which part of the string to index using [] around the position of the character you want to index; Index syntax is &#60;string&#62; [expression]; position 0 equals the first character; you can use negative numbers to start counting from the back of the string; Python will produce an error if you refer to a position that does not exist',
        'If the start expression is missing, the sub-sequence starts from the beginning of the string; if the stop expression is missing, the sub-sequence goes to the end of the string; start and end expressions having the same value results in an empty string; start expression and end expression which are consecutive (e.g. 3:4) will return the fourth character in the string; 3:6 will give the fourth and fifth characters; etc. Sub-sequence will work even when we reference positions that do not exist (unlike indexing)',
        'Finding strings within strings - use the find method (this is case sensitive) - this method outputs the position of the string where the specified sub-string is found; &#60;search string&#62;.find(&#60;target string&#62;)',
        'If the target string is not found in the search string when performing the find method, a negative 1 is returned',
        'Find method can also have a number parameter - the number is the position in the search string where the find will start looking for the target string;&#60;search string&#62;.find(&#60;target string&#62;, &#60;number&#62;)',
        'Triple quotes are used to create a multi-line string',
        'Edge cases - common cause of bugs in programming; '' is an empty string - so if s = "" then s[0] will cause an error because there is no character at position 0',
        'Extracting links from web pages - use the find method and look for the anchor tags',]),end_list(),end_sub_topic()

print start_sub_topic('Python - Functions'),start_list(), HTML_for_lists(['Functions or Procedures - used to map (take) inputs, perform some type of task to that input, then produce an output; you call or use a procedure using the syntax &#60;procedure&#62;(&#60;input1&#62;,&#60;input2&#62;,...). Syntax to create/ make/ define the procedure so it is available in the code to be used is <b>def <i>procedure_name</i>(<i>input1</i>, <i>input2</i>,...):</b> then the <b><i>body</i></b> and finally the <b> return <i>output</i></b>; the body is where the code is written that specifies what to do with the input parameters; an error message (or invalid output) will be returned if there is invalid syntax used, e.g. missing the <b>return</b> statement',
    'Inputs - operands/ arguments - these are parameters / values that get passed to the function and used within the function so the function can output the result',
    'Output - this is the result returned by the function after it is called and processes the input/ does the task',
    'After a procedure is called, the <b>return</b> statement returns to the code directly after where the procedure was called from',
    'Procedures are critical to use in coding to avoid repetition - once they are created they can be reused throughout then entire program (e.g. there may be multiple times in a program where two numbers need to be added together - instead of coding the addition formula each time, you can simply call one procedure that has been created to add two numbers together and return the result)',]),end_list(),end_sub_topic()

print start_sub_topic('Python Decisions and Repetitions'),start_list(),HTML_for_lists(['Making decisions - comparisons can use operators and boolean values and are used to make decisions (&60; &62; = which means assignment, != which means not equal to; == which means equality comparison - results in a true or false depending on whether the values match or not, AND, OR, etc.)',
    'OR - <i>Expression</i> or <i>Expression</i> - if the first expression evaluates to True, the value is True and the second expression is not evaluated; if the value of the first expression is False, the value is the value of the second expression.',
    'IF - syntax: IF <i>Test Expression</i>: and then on a new indented line, contains the <i>Block</i> which is what the program will do if the test expression is true; then the IF ends on a new line with same indentation as the IF, and this line executes if the expression was false (you can also use ELSE: to perform the steps if the expression was false). You can use nested IF statements.',
    'Loops - way to do things multiple time WHILE - similar syntax to IF. WHILE will execute as long as test expression remains True; the loop will end when the test expression is False. Be careful to not code Infinite loops (loop never ends).',
    'BREAK statement - gives a way to stop the loop even while the test condition is true; this is coded within the block section of the WHILE loop - use an IF to execute the BREAK (will break if IF test if True). The BREAK brings program to statement after the WHILE loop code.']),end_list(),end_sub_topic()

print start_sub_topic('Python Debugging'),start_list(),HTML_for_lists(['Program bugs - need to develop a strategy to identify and resolve bugs',
    'Program may crash with an error message, which can help trace back to the line of code the program ended at. This gives a starting place to begin looking at where the error may exist (there or in upstream code). You can also lookup the error messages to get more details.',
    'Bugs can also occur without the program crashing, but when the program is not giving the correct result; to resolve these types of bugs, you should break down your code to smaller pieces so as to identify which step the error is occurring in. Using PRINT statements can be useful to see the values of variables in different parts of the code.',
    'Five debugging strategies - 1) Examine error messages when program crashes; 2) Work from example code; 3) Make sure examples work; 4) Check/ print intermediate results; and 5) keep and compre old versions.']),end_list(),end_sub_topic()

print start_sub_topic('Python Lists and FOR Loops; Structured Data'),start_list(),HTML_for_lists(['Lists - whereas a String is a sequence of characters, a List is a sequence of anything.',
    'A String gets assigned to a variable with the string text contained inside quotes; a List is is assigned to a variable and defined inside of brackets, with each item in the list separated by a comma - items can be a mix of strings, numbers, or even other lists, including nested lists.',
    'You access an item in a String using variable name then 0 inside of brackets, e.g. S = "sometypeoftext" and S[0] would equal "s"; to access multiple characters of the string, use S[2:4] which would equal "me". Remember, lists are indexed starting at 0.',
    'You access items in a list also using brackets; if the list is assigned to the variable L, then L[0] will equal the first element in the list; using L[2:4] would equal the 3rd and 4th element in the list.',
    'l = [] creates an empty list "l" (0 elements); l = [a] creates a list "l" with one element which has the value of "a"; l = [a,b,c] creates a list "l" with three elements "a", "b", and "c". Elements in a list can be accessed by directly referencing the element number, or in "slices" using the format like part_of_list = l[1:].',
    'You can split the list code into multiple lines in Python for easier reading, but always split the line at a comma, and use indentation so the code is readable and it is clear that all lines are part of the same list.',
    'When using nested lists, you can access just one or more elements within the nested list, e.g. print l[3][0] which would return the 1st element within  the 4th element (nested list) in the main list.',
    'Lists support mutations - a mutation means the value of a list can be changed after its been created. E.g. to change the value of the 1st element in list l, you can code l[0] = "new value".',
    'NOTE - if you code multiple variables to equal the same list (or object) this is called aliasing - if you mutate elements of the list or object from any of the aliased variables, then all aliased variables will be assigned the mutated values even though only one of the aliased variables did the mutation. If you want, you can assign a new list to one of the alias variables, then this disassociates that variable from the other aliases.',
    'To add/ append a new element to the end of an existing list using the APPEND method, e.g. l.append("new element to add").',
    'The plus operation behaves similar to concatenation; this creates a new list which is the combination of the two or more lists that are in the + statement.',
    'The LEN operator (length) is used to return the number of elements in the object referenced in the LEN statement (can be used on strings, lists, etc.); e.g. len([0,1]) would output 2. LEN only counts the outer elements, not any nested list elements.',
    'FOR loops - can be used with lists; syntax is: for <i>name</i> in <i> list</i>: and then the next indented line is the code to perform in the loop; then the return statement.',
    'INDEX operator - you pass in a value target, and the output in index is the first position that the value is found in the list; syntax: <i>variable</i>.index(<i>target</i>). If the value is not found in the list, an error message will be returned saying "<i>target</i> is not in list".',
    'IN - syntax: "<i>value</i> in <i>list</i>", e.g. 3 in p; if the value is found in the list, the output is True, otherwise the output is False.',
    'NOT IN - can be used the same as IN, but with the opposite meaning.',
    'Solving problems 1 - first make sure you understand the problem before writing code; and determine what the inputs will be. Make sure to understand any assumptions/ requirements to ensure the code is able to handle any possibly condition. Determine how the inputs will be represented (e.g. how many parameters, etc.)',
    'Solving problems 2 - second thing to do is to identify what the outputs the code is supposed to produce.',
    'Solving problems 3 - third step is to solve the problem; begin by working out some examples which can then also be used as test cases to ensure the code is producing the desired output; understand the relationship between the input and outputs; make sure you can solve the problem systematically, as a human would.',
    'Writing pseudocode helps to break down how the program should be written. Keep the mechanical solution as simple as possible',
    'When you begin writing code, write structure small sections and test, and continue building upon this until you have solved the problem.',
    'Concatenating with .append() - append will add an element to the end of a list.',
    'Operator += - this copies the right-side elements into the original array.']),end_list(),end_sub_topic()

print end_lesson()