{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.0\n"
     ]
    }
   ],
   "source": [
    "num1 = input(\"Enter the 1st number: \")\n",
    "num2 = input(\"Enter the 2nd number: \")\n",
    "calcu = input(\"+, -, * or /\")\n",
    "\n",
    "if calcu == \"+\":\n",
    "    result = (float(num1) + float(num2))\n",
    "elif calcu == \"-\":\n",
    "    result =  (float(num1) - float(num2))\n",
    "elif calcu == \"*\":\n",
    "    result =  (float(num1) * float(num2))\n",
    "elif calcu == \"/\":\n",
    "    result =  (float(num1) / float(num2))\n",
    "else:\n",
    "    print (\"INVALID INPUT - Please enter proper number\")\n",
    "    result = None # none means no value whereas false means its wrong\n",
    "if result != None: # used != instead of is not\n",
    "    print (result)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
