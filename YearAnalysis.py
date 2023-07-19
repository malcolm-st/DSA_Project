import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_year_chart(year):
    # Check if the chart attribute exists in the year frame
    chart_attribute_exists = hasattr(year, "chart")

    if chart_attribute_exists:
        # If the attribute exists, remove the previous chart
        year.chart.get_tk_widget().pack_forget()
    else:
        # If the attribute doesn't exist, create it
        year.chart = None

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('CVECSV.csv')

    # Extract the year from the CVE ID
    df['Year'] = df['CveID'].str.extract(r'CVE-(\d{4})-\d+')

    # Count the number of CVEs for each year
    year_counts = df['Year'].value_counts()

    # Find the top five years with the most CVEs
    top_five_years = year_counts.nlargest(5).sort_values()

    # Display the CVE details for the top five years
    top_five_years_cves = df[df['Year'].isin(top_five_years.index)]

    # Create a bar chart of the top five years with the most CVEs
    fig, ax = plt.subplots()
    ax.bar(top_five_years.index, top_five_years.values)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of CVEs')
    ax.set_title('Top Five Years with the Most CVEs')

    # Embed the Matplotlib graph in the Year Page
    canvas = FigureCanvasTkAgg(fig, master=year)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Assign the chart attribute in the year frame
    year.chart = canvas