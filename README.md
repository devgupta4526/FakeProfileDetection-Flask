

# Fake Profile Detection Using Machine Learning

![Screenshot 2024-09-06 130407](https://github.com/user-attachments/assets/0b0fbd5c-c2c1-4389-9de4-1fa234275c87)



## Project Overview

This project focuses on detecting fake profiles on Instagram using advanced machine learning techniques. Our approach combines various classifiers and ensemble learning methods to enhance accuracy and robustness in identifying fraudulent accounts. We employ Gradient Boosting, Random Forest, and Support Vector Machine (SVM) models, alongside ensemble learning techniques, to achieve our objectives.


**Project Title:** Fake Profile Detection Using Machine Learning  
 
## Table of Contents

1. [Introduction](#introduction)
2. [Literature Review](#literature-review)
3. [Dataset](#dataset)
4. [Methodology](#methodology)
5. [Results & Conclusion](#results--conclusion)
6. [Contact](#contact)

## Introduction

Our project implements a robust system for detecting fake Instagram profiles using machine learning. We focus on data visualization, outlier handling, and feature engineering to enhance model performance. By leveraging classifiers such as Gradient Boosting, Random Forest, and SVM, our goal is to achieve accurate fake profile detection while mitigating overfitting and understanding feature importance.

## Literature Review

Here are some notable works in the field of fake profile detection:

| Sr No. | Author(s)/Year | Title | Findings/Relevance |
|--------|----------------|-------|---------------------|
| 1 | Eswara Venkata Sai Raja, Bhrugumalla L V S Aditya, Sachi Nandan Mohanty / 2023 | Fake Profile Detection Using Logistic Regression and Gradient Descent Algorithm on Online Social Networks | Achieved 92.7% accuracy with a false positive rate of 0.5% using Logistic Regression with Gradient Descent. |
| 2 | K. Harish, R. Naveen Kumar, Dr. J. Briso Becky Bell / 2023 | Fake Profile Detection Using Machine Learning | Demonstrates effective identification of fake profiles, with suggestions for applying the method to other platforms and real-time models. |
| 3 | Dr. K. SMITA, N. HARIKA, N. ADVAITHA, O. LAKSHMI KALYANI, T. KRUTHIKA / 2023 | Fake Profile Identification in Social Networks Using Machine Learning and NLP | Effective in identifying spammers on Twitter, with future directions including fake news detection and social network analysis. |
| 4 | Partha Chakraborty, Mahim Musharof Shazan, Mahamudul Nahid, Md. Kaysar Ahmed, Prince Chandra Talukder / 2022 | Fake Profile Detection Using Machine Learning Techniques | Highlights the use of machine learning for detecting fake profiles, with recommendations for combining models and real-time applications. |
| 5 | Ajith M, M. Nirmala / 2022 | Fake Accounts and Clone Profiles Identification on Social Media Using Machine Learning Algorithms | Effective in identifying fake and clone profiles on Twitter, with potential for extending to other platforms and using NLP techniques. |
| 6 | M. Mamatha, M. Srinivasa Datta, Umme Hani Ansari, Dr. Subhani Shik / 2021 | Fake Profile Identification Using Machine Learning Algorithms | Achieves high accuracy in detecting fake profiles, with future work focused on refining models and integrating real-time detection. |

## Dataset

The dataset used consists of 576 Instagram profiles with 12 features. The key features include:

- **Profile Picture:** Indicates if the account has a profile picture

- **Username Numeric Ratio:** Ratio of numerical characters in the username to its total length.
- **Full Name Words:** Number of words in the user's full name.
- **Full Name Numeric Ratio:** Ratio of numerical characters in the full name.
- **Name Matches Username:** Whether the username and full name are identical.
- **Description Length:** Character count of the user's bio.
- **External URL:** Presence of an external link in the bio.
- **Account Privacy:** Whether the account is private or public.
- **Number of Posts:** Total posts made by the user.
- **Number of Followers:** Number of users following the account.
- **Number of Follows:** Number of users the account follows.
- **Fake:** Target variable indicating if the account is classified as fake (1) or not (0).

## Methodology

1. **Data Loading and Exploration**
   - Imported necessary libraries and loaded the dataset.
   - Visualized distributions and identified outliers and correlations.

2. **Feature Engineering**
   - Introduced new features such as engagement ratio, social interaction index, profile completeness score, and average description word length.
   - Addressed missing values and transformed features with outliers.

3. **Data Preprocessing**
   - Split data into training and testing sets.
   - Standardized features using `StandardScaler`.

4. **Model Building and Evaluation**
   - Implemented classifiers: Gradient Boosting, Random Forest, and SVM.
   - Evaluated model performance and identified potential overfitting.

5. **Ensemble Learning**
   - Created an ensemble model using Voting Classifier with the base models.
   - Assessed performance of the ensemble model.

6. **Additional Analysis**
   - Explored the impact of removing certain features on model performance.

## Results & Conclusion

The ensemble model, combining Gradient Boosting, Random Forest, and SVM, demonstrated superior performance in detecting fake profiles compared to individual models. The evaluation metrics underscore its effectiveness and potential for practical application in combating fake profiles on social media platforms.

## Contact

For further inquiries or collaborations, please reach out to:

- **Twitter:** [@DevGupta4526](https://x.com/DevGupta4526)
- **Instagram:** [@underdroid_maven](https://www.instagram.com/underdroid_maven/)
- **Email:** [devguptamsi@gmail.com](mailto:devguptamsi@gmail.com)

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
