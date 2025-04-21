document.addEventListener("DOMContentLoaded", function() {
  const monthSelect = document.getElementById("month");
  const yearInput = document.getElementById("year");
  const generateBtn = document.getElementById("generate");
  const calendarBody = document.getElementById("calendar-body");

  // Set default values (January 2023)
  monthSelect.value = "0"; // January
  yearInput.value = "2023";

  // Define holidays for 2023 (this should be expanded for other years)
  const holidays2023 = {
    // Format: "MM-DD": "Holiday Name"
    "01-01": "New Year's Day",
    "01-02": "New Year's Holiday",
    // Add more holidays as needed
  };

  generateBtn.addEventListener("click", generateCalendar);

  // Generate the calendar on page load
  generateCalendar();

  function generateCalendar() {
    const month = parseInt(monthSelect.value);
    const year = parseInt(yearInput.value);

    // Clear previous calendar
    calendarBody.innerHTML = "";

    // Get the first day of the month
    const firstDay = new Date(year, month, 1);

    // Get the last day of the month
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();

    // Get the day of the week for the first day (0 is Sunday, 1 is Monday, etc.)
    let firstDayOfWeek = firstDay.getDay();
    // Convert Sunday (0) to 6 for our Monday-based week
    firstDayOfWeek = firstDayOfWeek === 0 ? 6 : firstDayOfWeek - 1;

    // Build the calendar
    let date = 1;
    let calendarHTML = "";

    // Create weeks until we've used all days
    for (let i = 0; i < 6; i++) {
      // Start a new row
      let row = "<tr>";

      // Fill in the days
      for (let j = 0; j < 7; j++) {
        if (i === 0 && j < firstDayOfWeek) {
          // Empty cells before the first day
          row += "<td></td>";
        } else if (date > daysInMonth) {
          // Empty cells after the last day
          row += "<td></td>";
        } else {
          // Regular day cell
          let dayClass = "";

          // Check if it's a weekend
          if (j === 5 || j === 6) {
            dayClass += "weekend ";
          }

          // Check if it's a holiday
          const dateStr = `${(month + 1).toString().padStart(2, "0")}-${date.toString().padStart(2, "0")}`;
          if (holidays2023[dateStr] && year === 2023) {
            dayClass += "holiday";
            row += `<td class="${dayClass}" title="${holidays2023}`
          }
        }
      }
    }
  }
}
