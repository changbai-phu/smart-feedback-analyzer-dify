## Background
While the existing workflows for customer feedback focus on classification and analysis, they can tell what the feedback is about, but often stop there. 

This workflow is designed to go one step further — helping teams decide what to do next. It is build on top of the existing template: **Customer Review Analysis Workflow** that provides a solid starting point for building more advanced workflows.


## Who this workflow is for
- Product Managers
- Operational Teams
- Small Business Owners

## Why I picked this problem
Customer feedback analysis is a common real worlf problem. It has a high impact because teams often receive large volumes of feedback, and handling it manually is time consuming. 

A well-designed workflow can improve efficiency and reduce manual work.

I also noticed many users on the Dify forum asking questions when building their own workflows. Many of these questions fall into the similar categories, such as: issues that may have already been solved before, real bugs that need attention, feature request and etc. 

This made me think it would be useful to build a workflow that not only analyzes feedback, but also helps guide next steps.

Before jumping into the ocean of the workflow, I explored existing templates in Dify and found the **Customer Review Analysis Workflow**. It has a strong foundation, so I decided to build on top of it and extend its capabilities step by step.


## How I used AI during the process
I used AI as a helper, but not as the final decision maker.
- I used AI to evaluate early ideas and compare options. 
- I also used AI to draft initial prompts, then manually refined them to make them clearer and more structured, making sure it is not overly simplified nor too general.
- I rejected overly complex designs suggested by AI, and focus on usability. 
- Debugging: AI was helpful for debugging, but not always correct. For instance, when I encountered the “output is missing” error, AI did not identify the issue correctly. After manual debugging, I found the real problem was a mismatch between the variable returned in the code node and the variable configured in Dify.

### Key design decisions
Initially, AI suggested four LLM nodes for classifications, insight extractor, priority, and action plan generation.
However, during testing, I found some crucial issues in that workflow:
- Information gets generalized too early 
- Important details are lost between steps
- Some steps repeat similar logic (e.g., priority requests were repeated)

To fix those, I changed the design:
- Keep LLM1 focused on structured classification
- Add a code node after LLM1 to count and aggregate data instead of using another LLM for summarization
- Use LLM2 to rank and select the top issues to focus on
- Use LLM3 to generate action plans based on the selected high priority issues, and original feedback input. 

This helps keep important context and reduces overlap between LLMs. 


## What you'd change with more time.
Due to time constraints, I focued on building a working version first. With more time, I would improve the workflow further:
 - Fix the full Test Run issue (manual node runs work, but full run may still cache)
 - Add a simple dashboard to visualize results
 - Add a feedback loop to improve results over time
 - Connect to real data source and extend to support file uploads(I did created a small CSV file for testing and successfully pass it to LLM nodes, but due to time constraints, had to put that on the side) -  For simplicity and clarity, I used text input for feedback in current version.




