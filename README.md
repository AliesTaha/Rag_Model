# DeepSeek RAG Model

A Retrieval-Augmented Generation (RAG) implementation using DeepSeek's language models.

## Overview

This project implements a RAG system that:

1. Takes a user query
2. Searches the web for relevant information using DuckDuckGo
3. Processes the retrieved content using DeepSeek Coder (1.3B instruct model)
4. Generates a comprehensive response based on the retrieved context

## Features

- Web search integration with DuckDuckGo
- Document retrieval and processing
- Vector embeddings using sentence-transformers
- FAISS vector database for efficient similarity search
- DeepSeek Coder 1.3B model for response generation

## Demo

- Question: What is the latest on DeepSeek models?

```
- Helpful Answer: DeepSeek has released several new models, 
including DeepSeek-V3, DeepSeek-R1, and DeepSeek Coder. 
These models are designed to perform better and more 
efficiently than their rivals, and they are all open source. 
They are available for free to use.
```

- Question: Who is Professor En-Hui Yang

```
Extracted Response: Professor En-Hui Yang is a faculty member in the 
Department of Electrical and Computer Engineering at the University 
of Waterloo since June 1997. He is a former Tier 1 Canada Research Chair 
holder in Information Theory and Multimedia Data Compression. He is the 
founding director of the Leitch-University of Waterloo multimedia communications 
lab, a co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry 
(formerly Research In Motion)), and the founder of BicDroid Inc. He currently 
serves as an Executive Council Member of the China Overseas Friendship 
Association, an Expert Advisor for the Overseas Chinese Affairs Office of the 
State Council of China, a member of IEEE Founders Medal Committee, and an 
advisor for other national and provincial bodies.
```

- Question: Who is Waterloo student Ali Taha

```
Extracted Response: Ali Taha is a 3rd-year Computer Engineering student at 
the University of Waterloo. He does Software Engineering and ML research.
```

^It extracts the above information by going directly to my website!

## How does it get this?

> Using device: cuda
Device set to use cuda

Extracted Response: Professor En-Hui Yang is a faculty member in the Department of Electrical and Computer Engineering at the University of Waterloo since June 1997. He is a former Tier 1 Canada Research Chair holder in Information Theory and Multimedia Data Compression. He is the founding director of the Leitch-University of Waterloo multimedia communications lab, a co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry (formerly Research In Motion)), and the founder of BicDroid Inc. He currently serves as an Executive Council Member of the China Overseas Friendship Association, an Expert Advisor for the Overseas Chinese Affairs Office of the State Council of China, a member of IEEE Founders Medal Committee, and an advisor for other national and provincial bodies.

The context it sees: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

En-Hui Yang | Electrical and Computer Engineering | University of Waterloo

Skip to main content

                      Jump to
                    





                              Jump to
                          





                      Admissions
                    





                      About Waterloo
                    





                      Faculties & Academics
                    





                      Offices & Services
                    





                      Support Waterloo
                    

Open Search Location
Search for

Search Location
On all sitesOn this site

Electrical and Computer Engineering

Menu

Electrical and Computer Engineering Home

                     About
                    





                              About
                          





                     Message from the Chair
                    





                     Program-Level Indicators
                    







                     Our people
                    





                              Our people
                          





                     Awards and honours
                    







                     Research
                    





                              Research
                          





                     Research Fields
                    





                     Research chairs, awards and honours
                    





                     Research seminars and lectures
                    





                     Research groups
                    





                     Research centres
                    







                     Resources
                    





                              Resources
                          





                     Safety in the ECE Undergraduate Programs
                    







                     News
                    





                     Events
                    





                              Events
                          





                     Distinguished Lecture Series
                    







                     Career opportunities
                    





                     Wellness
                    













                     Future students
                    





                     Undergraduate students
                    





                              Undergraduate students
                          





                     Academic advising
                    





                     Capstone design
                    





                     Co-op and careers
                    





                     Degree planning and enhancement
                    





                     Student life
                    





                     Scholarships and awards
                    





                     Meet our students
                    







                     Graduate students
                    





                              Graduate students
                          





                     Future Students
                    





                     Programs
                    





                     FAQ
                    







                     New Students
                    





                     Training Requirements
                    







                     Current Students
                    





                     Degree Requirements
                    





                     Courses
                    





                     ECE Graduate Course Archive
                    





                     Master of Engineering (Electric Power) courses Fall 2024 - Spring 2026
                    





                     Winter 2025 Courses
                    







                     Specializations
                    





                     Teaching Assistantships
                    





                     Student Services
                    





                     Student Life
                    







                     Research Fields
                    





                     Applied electromagnetics and photonics
                    





                     Artificial intelligence
                    





                     Biomedical engineering
                    





                     Communications and Information Systems
                    





                     Computer hardware
                    





                     Computer software and systems
                    





                     Control, robotics, and autonomous systems
                    





                     Integrated devices, circuits, and systems
                    





                     Nanoengineering
                    





                     Power and energy systems
                    





                     Quantum engineering
                    









                     Funding, Scholarships, Awards
                    





                     Meet our Graduate Students
                    





                     Alumni and friends
                    





                              Alumni and friends
                          





                     Alumni achievement awards and honours
                    





                     Alumni Gold Medal
                    





                     Alumni Achievement Awards
                    





                     UW 50th Anniversary Alumni Achievement Medals
                    





                     UW 60th Anniversary Alumni Awards
                    







                     Undergraduate Class Photos
                    







                     Faculty and staff
                    





                              Faculty and staff
                          





                     Computing support
                    





                     Faculty Performance
                    

±

En-Hui Yang

          University Professor
        
Email: <ehyang@uwaterloo.ca>

Location: EIT 4157
Phone: 519-888-4567 x32873
Multimedia Communications (Multicom) Laboratory

Biography
Dr. En-Hui Yang is a Professor in the Department of Electrical and Computer Engineering at the University of Waterloo and the founding Director of the Leitch-University of Waterloo Multimedia Communications Lab. He is also the co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry Inc., formerly known as Research In Motion) and a former associate editor for IEEE Transactions on Information Theory. Dr. Yang previously held a Tier 1 Canada Research Chair in Information Theory and Multimedia Data Compression.

Dr. Yang is known for co-developing the Yang-Kieffer algorithm, a numerical set of rules that use grammar-based coding to achieve lossless compression of text and image files. He is also the co-inventor of soft decision quantization (rate distortion optimization quantization or trellis quantization), an efficient coding technology used in image and video applications to improve compression, with widespread use in products like smartphones and web browsers.

His research interests span multimedia compression, information theory, digital communications, image and video coding, image understanding and management, big data analytics, information security, and deep learning. His work aims to develop technologies that enhance storage capacity of computers, accelerate and improve reliability of data transmission, improve data security, and make big data more understandable.

Dr. Yang is a Fellow of the Canadian Academy of Engineering, a Fellow of the IEEE, and a Fellow of the Royal Society of Canada. In 2024, he was honored with the title of 'University Professor' by the University of Waterloo in recognition of his exceptional scholarly achievements and international pre-eminence.
Research Interests

Multimedia Data Compression
Coding & Modulation
Information Theory
Digital Communications
Description Complexity Theory
Communication & Information Systems
Source & Channel Coding
Image & Video Coding
Multimedia Communications
Data Analytics
Information Security
Deep Learning

Education

1996, Doctorate Electrical Engineering, University of Southern California, United States
1991, Doctorate Probability and Statistics, Nankai University, China
1986, Bachelor's Applied Mathematics, HuaQiao University, China

Awards

2000, Ontario Premier's Research Excellence Award,  For research contributions to information theory and multimedia compression.
2001, Canada Research Chair (Tier 2), Information Theory and Multimedia Compression
2002,  Ontario Distinguished Researcher Award
2004, Outstanding Performance Award, University of Waterloo
2006, Canada Research Chair (Tier 2), Information Theory and Multimedia Compression
2010, Canada Research Chair (Tier 1),  Information Theory and its Applications
2009, Fellow of the Royal Society of Canada, En-Hui Yang is an international leader in source coding, a branch of information theory dealing with how to efficiently encode information for transmission, storage, and processing. A recipient of many awards including the 2007 Ernest C. Manning Award of Distinction and an IEEE Fellow, he has made profound contributions to communication engineering by introducing new fundamental source coding theory, solving long-standing open problems in source coding, inventing state-of-the-art lossless and lossy multimedia coding algorithms, co-founding SlipStream Data Inc., now a subsidiary of Research in Motion, and transforming his research results and coding algorithms into practice, which now impact on the daily life of tens of millions of people worldwide over 130 countries.
2009,  Fellow of the Canadian Academy of Engineering, En-Hui Yang is an international leader in source coding, a branch of information theory dealing with how to efficiently encode information for transmission, storage, and processing. A recipient of many awards including the 2007 Ernest C. Manning Award of Distinction and an IEEE Fellow, he has made profound contributions to communication engineering by introducing new fundamental source coding theory, solving long-standing open problems in source coding, inventing state-of-the-art lossless and lossy multimedia coding algorithms, co-founding SlipStream Data Inc., now a subsidiary of Research in Motion, and transforming his research results and coding algorithms into practice, which now impact on the daily life of tens of millions of people worldwide over 130 countries.
2007,  Ernest C. Manning Award of Distinction, For Outstanding Work in Creating, Developing and Commercializing Data Compression Technology That Has Significantly Improved the Speed and Efficiency of Digital Data and Image Transfer
2007,  Inaugural Ontario Premier's Catalyst Award, For the Development of Software for Data Acceleration
2008,  Distinguished Performance Award, Faculty of Engineering, University of Waterloo.
2008, Fellow of IEEE,  For Contributions to Source Coding
2008, Outstanding Performance Award, University of Waterloo
2013, CPAC Professional Achievement Award, For Outstanding Achievements in Information Theory and Related Areas.
2014,  IEEE Information Theory Society Padovani Lecture Award, For Contributions to Research in Information Theory and Related Areas
2014, FCCP Education Foundation Award of Merit, For Outstanding Achievements in Information Theory and Related Areas.
2017, Canada Research Chair (Tier 1),  Information Theory and its Applications
2018, Distinguished Overseas Scientist Award,  the Information Theory Society of Chinese Institute of Electronics
2021, IEEE Eric E. Sumner Award,  For Outstanding Contributions to Communications Technology
2021, elected Fellow, Asia-Pacific Artificial Intelligence Association
2023 Canadian Award for Telecommunications Research, Canadian Society of Information Technology
2024, University Professor, University of Waterloo

Teaching*

ECE 203 - Probability Theory and Statistics 1

Taught in 2022, 2023, 2024

ECE 307 - Probability Theory and Statistics 2

Taught in 2021

ECE 611 - Digital Communications

Taught in 2020, 2021

- Only courses taught in the past 5 years are displayed.

Selected/Recent Publications

He, J, Yang, En-Hui, Yang, F, and Yang, K, Adaptive Quantization Parameter Selection Algorithm for H.265/HEVC Based on Inter-Frame Dependency, IEEE Trans. Circuits Syst. Video Technology, 3424, 2018
Sun, Chang and Yang, En-Hui, An efficient DCT-based image compression system based on Laplacian transparent composite model, IEEE Transactions on Image Processing, 886, 2015
Yang, En-Hui and Meng, Jin, New Nonasymptotic Channel Coding Theorems for Structured Codes, IEEE Transactions on Information Theory, 4534, 2015
Yang, En-Hui and Yu, Xiang, Rate distortion optimization for H. 264 interframe coding: a general framework and algorithms, IEEE Transactions on Image Processing, 1774, 2007
Kieffer, John C and Yang, En-Hui, Grammar-based codes: a new class of universal lossless source codes, IEEE Transactions on Information Theory, 737, 2000

In The News

Prof honoured for impact on telecommunications

Graduate studies

            Currently considering applications from graduate students. A completed online application is required for admission; start the application process now.


            Has Sole-Supervisory Privilege Status (SSPS) status
          

Instagram

              Instagram
          

X (formerly Twitter)

                      X (formerly Twitter)
          

LinkedIn

              LinkedIn
          

Facebook

              Facebook
          

YouTube

              Youtube
          

University of Waterloo
200 University Ave W, Waterloo, ON
N2L 3G1
Phone: (519) 888-4567
Staff and Faculty DirectoryContact the Department of Electrical and Computer Engineering

  Support
  Waterloo
  Engineering

Waterloo Engineering Faculty OpeningsProvide Website FeedbackEngineering Website Help

University of Waterloo

University of Waterloo

43.471468
-80.544205

Campus map

              Campus map
          

200 University Avenue West

Waterloo,
      ON,
      Canada
N2L 3G1

+1 519 888 4567

                     Contact Waterloo
                    





                     Accessibility
                    





                     News
                    





                     Maps & directions
                    





                     Privacy
                    





                     Careers
                    





                     Emergency notifications
                    





                     Copyright
                    





                     Feedback
                    

The University of Waterloo acknowledges that much of our work takes place on the traditional territory of the Neutral, Anishinaabeg, and Haudenosaunee peoples. Our main campus is situated on the Haldimand Tract, the land granted to the Six Nations that includes six miles on each side of the Grand River. Our active work toward reconciliation takes place across our campuses through research, learning, teaching, and community building, and is co-ordinated within the Office of Indigenous Relations.

Instagram

              Instagram
          

X (formerly Twitter)

                      X (formerly Twitter)
          

LinkedIn

              LinkedIn
          

Facebook

              Facebook
          

YouTube

              YouTube
          

@uwaterloo social directory

On It Check

            WHERE THERE’S  A CHALLENGE,WATERLOO ISON IT.
          

Learn how   →

        ©2025 All rights reserved
      

About the Director | MultiCom Research Group | University of Waterloo

Skip to main content

                      Jump to
                    





                              Jump to
                          





                      Admissions
                    





                      About Waterloo
                    





                      Faculties & Academics
                    





                      Offices & Services
                    





                      Support Waterloo
                    

Open Search Location
Search for

Search Location
On all sitesOn this site

MultiCom Research Group

Menu

MultiCom Research Group Home

                     About us
                    





                     Research Team
                    





                              Research Team
                          





                     About the Director
                    





                     Memorable moments
                    





                     Awards and honors
                    







                     Publications
                    





                              Publications
                          





                     Refereed Conference Papers
                    





                     Technical Reports
                    





                     Patents
                    







                     Our sponsors
                    





                     Contact us
                    





                     Contacts
                    

±

About the Director

Meet Professor En-Hui Yang

En-hui Yang has been a faculty member in the Department of Electrical and Computer Engineering at the University of Waterloo since June 1997.  He is a former Tier 1 Canada Research Chair holder in Information Theory and Multimedia Data Compression. He is the founding director of the Leitch-University of Waterloo multimedia communications lab, a co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry (formerly Research In Motion)), and the founder of BicDroid Inc. He currently serves as an Executive Council Member of the China Overseas Friendship Association, an Expert Advisor for the Overseas Chinese Affairs Office of the State Council of China, a Board Trustee of Huaqiao University, a member of IEEE Founders Medal Committee, and an advisor for other national and provincial bodies.
He served as a Board Governor of the University of Waterloo; a Review Panel Member for the International Council for Science; an Evaluator for the 2017 Japan Prize (one of the most prestigious awards in science and technology fields after the Nobel Prize); an Associate Editor for IEEE Transactions on Information Theory; a general co-chair of the 2008 IEEE International Symposium on Information Theory, the largest premier international conference on information theory in the world; a technical program vice-chair of the 2006 IEEE International Conference on Multimedia & Expo (ICME); the chair of the award committee for the 2004 Canadian Award in Telecommunications; a co-editor of the 2004 Special Issue of the IEEE Transactions on Information Theory; a co-chair of the 2003 US National Science Foundation (NSF) workshop on the interface of Information Theory and Computer Science, the purpose of which is to advise NSF about research directions and support in the interface area; and a co-chair of the 2003 Canadian Workshop on Information Theory.
His research interests range from multimedia compression, information theory, digital communications, source and channel coding, image and video coding, deep learning and deep neural networks, to information security. He has exemplified research excellence in both theory and practice by introducing fundamental source coding theory; solving long- standing open problems in source coding; inventing state-of-the-art lossless and lossy compression algorithms for encoding text (such as web pages and emails), images, and video; designing the first-ever information theoretically secure key management protocols; inventing personalized and cryptographically secure access control in operating systems to enable data self-protection against known and unknown attacks; and transforming his theoretic results and algorithmic inventions into practice. With over 230 papers and more than 250 patents/patent applications worldwide, his research work has benefited people in over 170 countries through commercialized products, video coding open sources, and video coding standards. For example, his image and video coding algorithms and ideas are inside all communications and computing devices powered by Android 4.0 or higher, the number of which alone is in the billions; his data self-protection technologies are now incorporated into hundred millions of smart phones.
Dr. Yang is a Fellow of IEEE, a Fellow of the Canadian Academy of Engineering, and a Fellow of the Royal Society of Canada (The Academies of Arts, Humanities and Sciences of Canada). He is also a recipient of several awards and honors, including the 2021 IEEE Eric E. Sumner Award, the prestigious Inaugural Ontario Premier's Catalyst Award in 2007 for the Innovator of the Year (proceeds of the award were donated entirely to the University of Waterloo to create an annual En-hui Yang Engineering Research Innovation Award to encourage and support research and innovation - all Waterloo Engineering faculty are eligible to apply); the 2007 Ernest C. Manning Award of Distinction, one of Canada's most prestigious innovation prizes; the 2013 CPAC Professional Achievement Award; the 2014 IEEE Information Theory Society Padovani Lecture; the 2014 FCCP Education Foundation Award of Merit; Honorary Professor of Huaqiao University (2015), and the 2018 Distinguished Overseas Scientist Award from the Information Theory Society of Chinese Institute of Electronics. Products based on his early inventions and commercialized by his previous company, SlipStream, received the 2006 Ontario Global Traders Provincial Award. In 2011, he was selected for inclusion in Canadian Who's Who.

Professor Yang is the most all-around outstanding researcher and practitioner in the field of data compression, save the incomparable Claude E. Shannon who created information theory and in the process created the subject of data compression.

CRC referee’s praise for the nominee conveyed through NSERC.

University of Waterloo

University of Waterloo

43.471468
-80.544205

Campus map

              Campus map
          

200 University Avenue West

Waterloo,
      ON,
      Canada
N2L 3G1

+1 519 888 4567

                     Contact Waterloo
                    





                     Accessibility
                    





                     News
                    





                     Maps & directions
                    





                     Privacy
                    





                     Careers
                    





                     Emergency notifications
                    





                     Copyright
                    





                     Feedback
                    

The University of Waterloo acknowledges that much of our work takes place on the traditional territory of the Neutral, Anishinaabeg, and Haudenosaunee peoples. Our main campus is situated on the Haldimand Tract, the land granted to the Six Nations that includes six miles on each side of the Grand River. Our active work toward reconciliation takes place across our campuses through research, learning, teaching, and community building, and is co-ordinated within the Office of Indigenous Relations.

Instagram

              Instagram
          

X (formerly Twitter)

                      X (formerly Twitter)
          

LinkedIn

              LinkedIn
          

Facebook

              Facebook
          

YouTube

              YouTube
          

@uwaterloo social directory

On It Check

            WHERE THERE’S  A CHALLENGE,WATERLOO ISON IT.
          

Learn how   →

        ©2025 All rights reserved
      

Question: Who is Professor En Hui Yang?
Helpful Answer: Professor En-Hui Yang is a faculty member in the Department of Electrical and Computer Engineering at the University of Waterloo since June 1997. He is a former Tier 1 Canada Research Chair holder in Information Theory and Multimedia Data Compression. He is the founding director of the Leitch-University of Waterloo multimedia communications lab, a co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry (formerly Research In Motion)), and the founder of BicDroid Inc. He currently serves as an Executive Council Member of the China Overseas Friendship Association, an Expert Advisor for the Overseas Chinese Affairs Office of the State Council of China, a member of IEEE Founders Medal Committee, and an advisor for other national and provincial bodies.

## Requirements

- Python 3.8+
- LangChain
- Transformers
- PyTorch
- FAISS
- DuckDuckGo Search
- Sentence Transformers
- Hugging Face Hub

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/deepseek-rag.git
   cd deepseek-rag
   ```

2. Create a virtual environment (recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `rag.py` file and modify the query variable to ask your own question:

   ```python
   # Change this to your own query
   query = "What is the latest on DeepSeek models?"
   ```

2. Run the script:

   ```
   python rag.py
   ```

3. The script will:
   - Search the web for information related to your query
   - Process the retrieved documents
   - Generate a response using the DeepSeek Coder model
   - Print the extracted response and the full context

## Customization

- To use a different model, change the `model_name` variable in `rag.py`
- Adjust the number of search results by modifying the `max_results` parameter in the `search_and_scrape` function
- Change the embedding model by updating the `model_name` in the `create_retriever` function
