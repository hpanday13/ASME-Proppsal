import streamlit as st

# Initialize a variable to keep track of the total project cost
total_project_cost = 0

# Title of the Streamlit app
st.title('Proposal for ME Research Project')

# Introductory text
st.markdown("""
This calculator estimates the costs associated with conducting desk research on the Mechanical Engineering (ME) academic and employment ecosystem across India.""")

# Function to add section costs to the total project cost and display them
def display_and_add_to_total(section_title, section_cost):
    global total_project_cost
    total_project_cost += section_cost
    st.markdown(f"**{section_title} Cost: USD {section_cost:,.2f}**")
    
st.divider()
st.write("Gathering data on enrollment levels, placement rates, and academic offerings is challenging due to the dispersed nature of information. This necessitates individualized searches and the curation of datasets for later analysis")
# Creating two columns for input fields
col1, col2 = st.columns(2)

# Inputs in the first column
with col1:
    num_colleges = st.slider('Number of Colleges Surveyed', 1, 100, 50, help="Adjust the number of engineering colleges included in the survey.", key='num_colleges_dr')
    hours_collection_per_college = st.number_input('Average Hours of Data Collection per College', 1.0, 10.0, 5.0,
                                                    help="Estimated hours needed to collect data per college.", key='hours_collection_per_college_dr')
    rate_collection = st.number_input('Hourly Rate for Data Collection (USD)', 10, 50, 20,
                                       help="The cost per hour for professionals collecting the data.", key='rate_collection_dr')

# Inputs in the second column
with col2:
    hours_analysis = st.number_input('Total Hours for Data Analysis', 50, 200, 100,
                                     help="Total hours anticipated for analyzing the collected data.")
    rate_analysis = st.number_input('Hourly Rate for Data Analysis (USD)', 20, 50, 30,
                                    help="The cost per hour for data analysis.")
    fixed_costs = st.number_input('Fixed Costs for Software and Miscellaneous (USD)', 0, 1000, 500,
                                  help="Estimated fixed costs for software and other expenses.")

# Calculating the total costs based on the input values
total_collection_cost = num_colleges * hours_collection_per_college * rate_collection
total_analysis_cost = hours_analysis * rate_analysis
desk_research_cost = total_collection_cost + total_analysis_cost + fixed_costs
display_and_add_to_total("Desk Research", desk_research_cost)


st.divider()
st.markdown("""
Estimate the costs associated with conducting primary research on student perspectives in the Mechanical Engineering (ME) domain. This research aims to understand motivations for enrolling in ME, reasons for opting out, and perceptions influencing these decisions, including factors like starting salaries, parental pressure, and societal views. Choose between virtual and in-person interviews to see how it impacts the cost.
""")

# Option to select interview mode
interview_mode = st.radio("Interview Mode", ('In-Person', 'Virtual'), help="Select the mode of conducting interviews with students.")

# Creating columns for input fields to organize the UI
col1, col2, col3 = st.columns(3)

# Inputs for the number of colleges and students to be surveyed
with col1:
    num_colleges = st.number_input('Number of Colleges Surveyed', min_value=1, max_value=100, value=10,
                                   help="The number of colleges from which students will be surveyed.")
    num_students_per_college = st.number_input('Students Surveyed per College', min_value=10, max_value=200, value=50,
                                               help="The average number of students surveyed at each college.")

# Inputs for travel costs and incentives for participation, adjusted by interview mode
with col2:
    if interview_mode == 'In-Person':
        avg_travel_cost = st.number_input('Average Travel Cost per College (USD)', min_value=0, max_value=5000, value=1000,
                                          help="Average travel and accommodation cost for conducting surveys at each college.")
    else:
        avg_travel_cost = 0  # No travel cost for virtual interviews
    incentive_per_student = st.number_input('Incentive per Student Surveyed (USD)', min_value=0, max_value=100, value=10,
                                            help="Financial incentive provided to each student for participating in the survey.")

# Inputs for data analysis and miscellaneous costs
with col3:
    hours_analysis = st.number_input('Hours Spent on Data Analysis', min_value=10, max_value=500, value=100,
                                     help="Total hours required for data analysis.")
    hourly_rate_analysis = st.number_input('Hourly Rate for Data Analysis (USD)', min_value=10, max_value=100, value=30,
                                           help="The cost per hour for professionals analyzing the data.")
    misc_costs = st.number_input('Miscellaneous Costs (USD)', min_value=0, max_value=5000, value=500,
                                 help="Estimated miscellaneous costs including software, communication, and unforeseen expenses.")

# Calculate the total cost based on input values
total_students = num_colleges * num_students_per_college
total_travel_cost = num_colleges * avg_travel_cost
total_incentive_cost = total_students * incentive_per_student
primary_research_students_cost = total_travel_cost + total_incentive_cost + total_analysis_cost + misc_costs
display_and_add_to_total("Primary Research on Students", primary_research_students_cost)

st.divider()

# Introduction
st.markdown("""
Estimate the costs associated with scraping job data for Mechanical Engineering (ME) to analyze the current employer market. This includes developing a web scraper, collecting data on job postings, storing the data, and conducting a detailed analysis to identify market trends and patterns.
""")

# Creating columns for input fields to organize the UI
col1, col2 = st.columns(2)

# Inputs for the development and operation of web scraper
with col1:
    dev_hours = st.number_input('Development Hours for Web Scraper', min_value=10, max_value=200, value=50,
                                help="Total hours required to develop the web scraper.")
    dev_hourly_rate = st.number_input('Hourly Rate for Development (USD)', min_value=10, max_value=100, value=30,
                                      help="The cost per hour for the developer working on the web scraper.")
    num_sites = st.number_input('Number of Sites to Scrape', min_value=1, max_value=50, value=5,
                                help="The number of job listing sites to scrape for data.")
    operation_costs = st.number_input('Operational Costs (USD)', min_value=0, max_value=1000, value=100,
                                      help="Costs associated with running the scraper, including server and proxy costs.")

# Inputs for data analysis
with col2:
    analysis_hours = st.number_input('Hours Spent on Data Analysis', min_value=20, max_value=500, value=100,
                                     help="Total hours required for analyzing the scraped job market data.")
    analysis_hourly_rate = st.number_input('Hourly Rate for Data Analysis (USD)', min_value=20, max_value=100, value=40,
                                           help="The cost per hour for professionals analyzing the data.")
    storage_costs = st.number_input('Data Storage Costs (USD)', min_value=0, max_value=500, value=50,
                                    help="Estimated costs for storing the scraped data.")

# Calculate the total cost based on input values
total_development_cost = dev_hours * dev_hourly_rate
total_analysis_cost = analysis_hours * analysis_hourly_rate
job_market_analysis_cost = total_development_cost + operation_costs + total_analysis_cost + storage_costs
display_and_add_to_total("Job Market Analysis", job_market_analysis_cost)

st.divider()
st.markdown("""
Estimate the costs associated with conducting primary research on employer perspectives within the Mechanical Engineering (ME) domain. This research aims to understand where employers are sourcing their ME talent from, the filters they apply in the selection process, the extent and focus of upskilling required to make the talent viable, and specific areas of upskilling.
""")

# Option to select interview mode
interview_mode = st.radio("Interview Mode", ('In-Person', 'Virtual'), help="Select the mode of conducting interviews with employers.")

# Creating columns for input fields to organize the UI
col1, col2, col3 = st.columns(3)

# Inputs for the number of employers to be surveyed
with col1:
    num_employers = st.number_input('Number of Employers Surveyed', min_value=1, max_value=100, value=30,
                                    help="The number of employers to be surveyed for the research.")

# Inputs for interview costs, adjusted by interview mode
with col2:
    if interview_mode == 'In-Person':
        avg_travel_cost_per_employer = st.number_input('Average Travel Cost per Employer (USD)', min_value=0, max_value=5000, value=500,
                                                       help="Average travel and accommodation cost for conducting surveys with each employer.")
    else:
        avg_travel_cost_per_employer = 0  # No travel cost for virtual interviews
    incentive_per_employer = st.number_input('Incentive per Employer Surveyed (USD)', min_value=0, max_value=500, value=100,
                                             help="Financial incentive provided to each employer for participating in the survey.")

# Inputs for data analysis and miscellaneous costs
with col3:
    hours_analysis = st.number_input('Hours Spent on Data Analysis', min_value=10, max_value=500, value=120,
                                     help="Total hours required for data analysis.")
    hourly_rate_analysis = st.number_input('Hourly Rate for Data Analysis (USD)', min_value=10, max_value=100, value=40,
                                           help="The cost per hour for professionals analyzing the data.")
    misc_costs = st.number_input('Miscellaneous Costs (USD)', min_value=0, max_value=5000, value=1000,
                                 help="Estimated miscellaneous costs including software, communication, and unforeseen expenses.")

# Calculate the total cost based on input values
total_travel_cost = num_employers * avg_travel_cost_per_employer
total_incentive_cost = num_employers * incentive_per_employer
total_analysis_cost = hours_analysis * hourly_rate_analysis
employer_research_cost = total_travel_cost + total_incentive_cost + total_analysis_cost + misc_costs
display_and_add_to_total("Primary Research on Employers", employer_research_cost)


st.divider()

# Introduction
st.markdown("""
Estimate the costs associated with conducting primary research on the perspectives of academics and academic administration in the Mechanical Engineering (ME) domain. This research aims to understand recruitment strategies for applicants, curriculum effectiveness, the frequency of updates, connections with employers, skill alignment, and other challenges in academia.
""")

# Option to select interview mode
interview_mode = st.radio("Interview Mode", ('In-Person', 'Virtual'), help="Select the mode of conducting interviews with academic staff.")

# Creating columns for input fields to organize the UI
col1, col2, col3 = st.columns(3)

# Inputs for the number of academic institutions to be surveyed
with col1:
    num_institutions = st.number_input('Number of Academic Institutions Surveyed', min_value=1, max_value=100, value=20,
                                       help="The number of academic institutions to be surveyed for the research.")

# Inputs for interview costs, adjusted by interview mode
with col2:
    if interview_mode == 'In-Person':
        avg_travel_cost_per_institution = st.number_input('Average Travel Cost per Institution (USD)', min_value=0, max_value=5000, value=300,
                                                          help="Average travel and accommodation cost for conducting surveys with each academic institution.")
    else:
        avg_travel_cost_per_institution = 0  # No travel cost for virtual interviews
    incentive_per_institution = st.number_input('Incentive per Academic Institution Surveyed (USD)', min_value=0, max_value=500, value=50,
                                                help="Financial incentive provided to each institution for participating in the survey.")

# Inputs for data analysis and miscellaneous costs
with col3:
    hours_analysis = st.number_input('Hours Spent on Data Analysis', min_value=10, max_value=500, value=100,
                                     help="Total hours required for data analysis.", key='acad_hours_analysis')
    hourly_rate_analysis = st.number_input('Hourly Rate for Data Analysis (USD)', min_value=10, max_value=100, value=35,
                                           help="The cost per hour for professionals analyzing the data.", key='acade_hourlyrate_dr')
    misc_costs = st.number_input('Miscellaneous Costs (USD)', min_value=0, max_value=5000, value=750,
                                 help="Estimated miscellaneous costs including software, communication, and unforeseen expenses.", key='misc_cost_dr')

# Calculate the total cost based on input values
total_travel_cost = num_institutions * avg_travel_cost_per_institution
total_incentive_cost = num_institutions * incentive_per_institution
total_analysis_cost = hours_analysis * hourly_rate_analysis
acad_research_cost = total_travel_cost + total_incentive_cost + total_analysis_cost + misc_costs
display_and_add_to_total("Academia Primary Research", acad_research_cost)


st.divider()
# Introduction
st.markdown("""
Estimate the costs associated with conducting a detailed analysis of the collected data and formulating recommendations for ASME, industry, academia, and students to improve the Mechanical Engineering (ME) ecosystem. This includes expert analysis, stakeholder meetings, and report development.
""")

# Creating columns for input fields to organize the UI
col1, col2, col3 = st.columns(3)

# Inputs for analysis and stakeholder engagement
with col1:
    analysis_hours = st.number_input('Hours Spent on Detailed Analysis', min_value=50, max_value=500, value=100,
                                     help="Total hours required for conducting a detailed analysis of the collected data.")
    analysis_hourly_rate = st.number_input('Hourly Rate for Analysis (USD)', min_value=20, max_value=100, value=50,
                                           help="The cost per hour for professionals performing the analysis.")

# Inputs for report writing and recommendations
with col2:
    report_hours = st.number_input('Hours Spent on Report Writing', min_value=20, max_value=200, value=50,
                                   help="Total hours required for writing the comprehensive report, including recommendations.")
    report_hourly_rate = st.number_input('Hourly Rate for Report Writing (USD)', min_value=20, max_value=100, value=40,
                                         help="The cost per hour for professionals writing the report.")

# Inputs for miscellaneous costs
with col3:
    stakeholder_meetings = st.number_input('Number of Stakeholder Meetings', min_value=1, max_value=20, value=5,
                                           help="Number of meetings with stakeholders to gather insights and feedback.")
    cost_per_meeting = st.number_input('Cost per Meeting (USD)', min_value=0, max_value=2000, value=500,
                                       help="Estimated costs per meeting, including logistics and possible incentives for participants.")
    misc_costs = st.number_input('Miscellaneous Costs (USD)', min_value=0, max_value=5000, value=1000,
                                 help="Estimated miscellaneous costs, including communication and unforeseen expenses.")

# Calculate the total cost based on input values
total_analysis_cost = analysis_hours * analysis_hourly_rate
total_report_cost = report_hours * report_hourly_rate
total_meeting_cost = stakeholder_meetings * cost_per_meeting
reco_analysis_cost = total_analysis_cost + total_report_cost + total_meeting_cost + misc_costs
display_and_add_to_total("Analysis and Recommendation Report", reco_analysis_cost)

st.divider()
# Introduction
st.markdown("""
Estimate the costs associated with producing and disseminating a high-quality research report aimed at impacting the Mechanical Engineering (ME) ecosystem at a pan-India scale. This includes costs for professional writing, editing, graphic design, printing, and wide dissemination.
""")

# Creating columns for input fields to organize the UI
col1, col2 = st.columns(2)

# Inputs for professional services and production
with col1:
    writing_editing_hours = st.number_input('Hours for Writing and Editing', min_value=50, max_value=1000, value=200,
                                            help="Total hours required for professional writing and editing of the report.")
    hourly_rate_writing_editing = st.number_input('Hourly Rate for Writing and Editing (USD)', min_value=20, max_value=100, value=50,
                                                  help="The cost per hour for professional writers and editors.")
    graphic_design_hours = st.number_input('Hours for Graphic Design', min_value=10, max_value=500, value=100,
                                           help="Total hours required for graphic design work for the report.")
    hourly_rate_graphic_design = st.number_input('Hourly Rate for Graphic Design (USD)', min_value=20, max_value=150, value=60,
                                                 help="The cost per hour for professional graphic designers.")

# Inputs for printing and dissemination
with col2:
    num_copies = st.number_input('Number of Printed Copies', min_value=0, max_value=5000, value=1000,
                                 help="Total number of copies to be printed for distribution.")
    cost_per_copy = st.number_input('Cost per Printed Copy (USD)', min_value=1, max_value=10, value=2,
                                    help="Cost for printing each copy of the report.")
    digital_dissemination_costs = st.number_input('Digital Dissemination Costs (USD)', min_value=0, max_value=5000, value=1000,
                                                  help="Costs associated with digital dissemination, including hosting, distribution platforms, and promotional activities.")

# Calculate the total cost based on input values
total_writing_editing_cost = writing_editing_hours * hourly_rate_writing_editing
total_graphic_design_cost = graphic_design_hours * hourly_rate_graphic_design
total_printing_cost = num_copies * cost_per_copy
report_production_cost = total_writing_editing_cost + total_graphic_design_cost + total_printing_cost + digital_dissemination_costs
display_and_add_to_total("Final Report Production and Dissemination", report_production_cost)

st.divider()

# Display the total estimated cost for the entire project
st.header("Total Project Cost")
st.markdown(f"### Total Estimated Funds Needed: USD {total_project_cost:,.2f}")