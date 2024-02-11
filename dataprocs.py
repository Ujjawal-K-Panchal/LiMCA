"""
Title: Data Processes.

Date: Feb 10, 2024

Author: Ujjawal K. Panchal
"""
import re, warnings, os
from pathlib import Path
from typing import List, Dict

import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

from leetscrape import GetQuestionsList, GetQuestion, models

warnings.filterwarnings("ignore")

#savefile.
datafolder = Path("data")
if not os.path.exists(datafolder):
    os.makedirs(datafolder)

lc_savefile = datafolder  / "leetcode.csv"


def getLCTestCases(question: models.Question) -> List[Dict]:
    #find tags.
    cases = BeautifulSoup(question.Body).findAll("pre") 
    # regex for cases.
    input_pattern = re.compile(r'<strong>Input:</strong>(.*?)<strong>', re.DOTALL)
    output_pattern = re.compile(r'<strong>Output:</strong>(.*?)<strong>', re.DOTALL)
    exp_pattern = re.compile(r'<strong>Explanation:</strong>(.*?)<strong>', re.DOTALL)

    #add all cases.
    case_list = []
    for case in cases:
        input_find = input_pattern.search(str(case)) 
        output_find = output_pattern.search(str(case))
        exp_find = exp_pattern.search(str(case))
        #add params if found.
        case_dict = {
            'inputs': input_find.group(1).strip() if input_find else None,
            'outputs': output_find.group(1).strip() if output_find else None,
            'explanation': exp_find.group(1).strip() if exp_find else None,
        }
        case_list.append(case_dict)

    #return all cases.
    return case_list

def getLCDescription(question_text: str) -> str:
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    # Use a specific pattern to match the question description without HTML tags and examples
    pattern = re.compile(r'<p>(.*?)<\/p>', re.DOTALL)

    # Find all matches
    matches = pattern.findall(question_text)

    # Extract and return the description without examples and HTML tags
    description = matches[0].strip() if matches else "No description found."

    # Exclude examples
    description = re.sub(r'<strong class="example">.*?<\/strong>', '', description)
    description = re.sub(r'<pre>.*?<\/pre>', '', description)

    # Remove all remaining HTML tags
    description = remove_html_tags(description)
    return description

def getLCQuestions() -> pd.DataFrame:
    ls = GetQuestionsList()
    ls.scrape()
    questions = []
    qdf = pd.DataFrame(columns = ['title', 'desc', 'difficulty', 'cases'])
    with tqdm(ls.questions.titleSlug, unit = "questions") as questioniter:
        for titleSlug in questioniter:
            try:
                question = GetQuestion(titleSlug = titleSlug).scrape()
                qdict = {
                    'title': question.title,
                    'desc': getLCDescription(question.Body),
                    'difficulty': question.difficulty,
                    'cases': getLCTestCases(question),
                }
                qdf = qdf.append(qdict, ignore_index = True)
            except Exception as e:
                print(f"Couldn't get question: {titleSlug}")
    return qdf

def saveLCQuestions(questions: pd.DataFrame, filename: Path | str) -> None:
    questions.to_csv(filename)
    return

def downloadLCQuestions(savefile: str = lc_savefile):
    #1. get all leetcode questions.
    questions = getLCQuestions()

    #2. save questions.
    saveLCQuestions(questions, savefile)
    return

if __name__ == "__main__":
    #1. download LeetCode questions.
    if os.path.exists(lc_savefile):
        print(f"LeetCode already downloaded.")
    else:
        downloadLCQuestions()
    #2. download Refactory questions.
        ...

    

        
    