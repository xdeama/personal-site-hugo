---
translationKey: blog_microservices
title: 'The Rise and Fall of Micro Services'
description: 'Developers are increasingly turning away from microservices - Explaining why to non-developers.'
date: 2023-11-17T10:15:00-01:00
draft: false
tags: 
  - microservices
---
## What are Microservices
Microservices are a form of architecture where an application is designed as a collection of small, independent services, each implementing specific business logic or functionalities. This architecture allows for high scalability and flexibility since individual services can be developed, deployed, and scaled independently. However, this distribution also leads to challenges in terms of integration, management, and security of the services.

## The Rise and Fall of Micro Services
Developers are increasingly turning away from microservices, as this architecture brings complex challenges related to integration, network latency, data consistency, and managing multiple independent services. Additionally, the increased complexity in troubleshooting and monitoring, as well as the need for advanced DevOps skills, can deter some teams from using microservices.

Microservices are not suitable as a de-facto industry standard and go-to solution for any application. However, they have been used in this way. And therefore, this sophisticated and ingenious form of architecture is currently experiencing a backlash.

In the following, I greatly simplified the topic of microservices using a limited analogy with Microsoft Excel to provide an insight into the subject for those unfamiliar with the field.

## The Rise
A bank issues loans, and to evaluate these loans, five departments need to receive and provide data. The data consists of loan application details and information previously determined and provided by other departments.

These five departments each receive their requests via email from the front office. Thus, days pass before the customer receives a response. In each department, specialists are tasked with daily operations: entering data from emails into their evaluation matrix and sending the results back to the front office via email.

In all cases, the evaluation matrix is a complex Excel sheet, updated daily with the latest parameters like interest rates, currency exchange rates, and the like.

{{< embed-svg "static/svg/spreadsheet.svg" >}}

To expedite the loan approval process, it is agreed to create a single merged Excel document containing an input form. The front office fills this form with customer data. The embedded logic calculates and determines the data previously transmitted by the five departments via email and displays it on the output form. The departments are to keep the logic and used data up to date so that most loan applications can be processed directly by the front office without further inquiries.

However, during the merging process into a single Excel document, it becomes apparent that only one of the 25 involved employees can edit the file at a time. While some changes of an additive nature can be prepared, they also require an exclusive time slot for integration into the overall document. This significantly slows progress and causes frustration, as everyone must wait in turn to access the document.

Furthermore, it is regularly discovered that one change has distorted the function of another. For instance, the interest risk department should have provided the valid interest rate for the other departments, but the field where it was written and the decimal places have been changed several times. This results in additional time lost, as each change can lead to further dependent changes.

An Excel architect is commissioned to make the project more technically efficient, enabling progress and capturing dissatisfaction.

The architect calls the Excel document (hereafter referred to as Bank Excel) a monolith and identifies this as the problem. He suggests splitting it into Micro Services, i.e., Micro Excels, meaning several individual Excel documents that automatically work together technically.

Each department will henceforth create and maintain its own Excel document (hereafter referred to as Department Excel). For automated collaboration in the shared Bank Excel, a workspace is created for each department's "Input" and the "Output" it delivers. Excel documents can both read from and write to other documents. (Please ignore any technical issues here for the purpose of the analogy.)

The content, i.e., the fields entered and their data format, is agreed upon in advance and cannot be easily adjusted. Thus, the departments have agreed on interfaces.

Now, each department independently undertakes what is necessary with the input data to produce the output data. If interest curves, logic for new legislation, or customer master data need to be adjusted, each department can do so without involving the others.

Only changes to the Bank Excel, i.e., the agreed-upon input and output worksheets, need to be coordinated with all departments.

The architect is praised and successfully discharged from the project. He has restored the autonomous operational capability of the departments and enabled automated collaboration with the Bank Excel.
## The Climax
The procedure becomes well-known; even the manufacturer offers improved tools for this type of Excel usage. Soon, all Excel documents are created in a distributed manner. The technology becomes very versatile and powerful. Not without consequences: the in-house IT had to upgrade the LAN of the sites and the WAN connections between them several times to accommodate the network traffic.
## The Fall
A year later, the bank decides to switch to a different Excel program. Microsoft Excel has an integrated AI that does not comply with European privacy laws.
At the same time a change from a comma to a dot as a decimal separator shall be implemented to be more internationally compatible.

The architect is re-hired to estimate the effort involved and offer a team of consultants.

The effort estimation reveals: since each Excel document was divided into up to 10 parts, instead of the 100 Bank Excel, an additional 1000 Department Excel documents need to be revised.

A second architect is involved to verify the estimate. The effort seems enormous to all involved, as only 100 Excel documents are used at the bank level.

The second architect confirms: the distributed architecture resulted in ten times the number of Excel documents and a significant increase in network traffic. One could significantly reduce the costs for migrations, computing power, network traffic, and data security by centralizing the Excel documents.

The management is outraged: are they being taken advantage of by the architect? Did he create this complex landscape to later profit from it?

After discussion and negotiation, it is decided:
- to maintain the distributed architecture wherever it fits the organizational structure of the bank and offers advantages for collaboration and timeliness of logic and data
- to remove the distributed architecture wherever the overall authority over all distributed Excel documents lies within a single department, no problems arise from sequential work on the document, and the documents do not exceed a maximum size

The bank now evaluates before developing any new system and

during further development whether the chosen architecture fits the application case.

## Conclusion
The advantages:
* Decentralized ownership
* Parallel development
* Improved scalability

do not come without disadvantages in organizational and technical complexity.

Moreover, Monolith and Micro Service are just two of many architectural patterns that offer advantages and disadvantages for your system.
