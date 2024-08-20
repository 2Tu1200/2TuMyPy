{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6bde8cbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# main.py\n",
    "\n",
    "from fastapi import FastAPI\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/\")\n",
    "async def root():\n",
    "    return {\"message\": \"Hello World\"}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85659911",
   "metadata": {},
   "source": [
    "# This is my First Standalone complete API, would run using Uvicorn on conda command promt, chek File1toBe for more. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3046d129",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3807844594.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [2]\u001b[1;36m\u001b[0m\n\u001b[1;33m    uvicorn main:app --reload\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "uvicorn main:app --reload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b4f8130",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3217600887.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [3]\u001b[1;36m\u001b[0m\n\u001b[1;33m    uvicorn main.py:app --reload\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "uvicorn main.py:app --reload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aae0bb3b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
