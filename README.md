<H2>OTS V1</H2>

Every end of the week, we receive our class schedule in the form of a PDF uploaded to a Dropbox folder. We receive this link as an announcement on the school's Facebook page.

The process seems simple: enter the school's Facebook page, check for the latest post, enter the link, and search for your class schedule among more than 15 classes. However, the issue arises when we can't download the schedule PDF without having other classes' schedules. Additionally, attempting to screenshot the schedule results in a blurry image. Furthermore, while trying to obtain the schedule, I may become confused with other posts on Facebook, leading to a loss of focus for an hour or more.

For these reasons, I thought, <b>"Why not create a Python script alongside a webpage to solve this issue for me?"</b>

![image](https://github.com/zakariaelharrak/ofpptemploidetemp/assets/58367411/0b63d137-bfeb-4127-9ed1-fe6d01c9f09e)

<H2>Problem</H2>

So... to solve this issue, I need to address these technical issues:

<li>I need to crop each PDF based on the timetable table. (Note: Some pages contain 2-3 tables.)</li>
<li>I need to organize and rename each PDF automatically with the class name.</li>
<li>I need to redesign this script in an interactive way, allowing users to select their class and access their school timeline in fewer than 3 clicks.</li>
<li>Finally, I want to deploy this solution using Azure web services to make it live.</li>

<H2>Soulotion</H2>
For the first issue, I experimented with various Python packages and settled on PyMuPDF. I implemented a method to split each PDF into three sections, each with a height of 250px. This resulted in a list of split PDFs, each dedicated to a single class.

Addressing the second issue, I utilized a variety of packages to first open all the PDFs and analyze them to search for the class names. Finally, the script renamed each PDF with its corresponding class name.

Subsequently, I developed a straightforward webpage featuring an option input containing all the class names (extracted from the PDFs resulting from splitting the main school schedule PDFs). I integrated a simple logic so that whenever a student selects one of the options (class names), their schedule is displayed using Flask.

![ots (1)](https://github.com/zakariaelharrak/ofpptemploidetemp/assets/58367411/1e94058b-26c9-4045-b436-08d6dc15e475)

Finally, for the last step of making this solution live, I deployed it using Azure web services. I installed necessary packages and executed the planned deployment, and everything functioned as intended.

https://ofpptemploidetemp.azurewebsites.net/


