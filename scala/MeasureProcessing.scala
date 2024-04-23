object MeasureProcessing {

  def get_measures_per_day(measure_per_hour : Seq[Int]) : Seq[Seq[Int]] = {
    /*
    Initialize an empty Seq[Seq[Int]]
    Get the number of days
    Slice measure_per_hour per day 
    Arg:
    measure_per_hour : Seq[Int]
    Return:
      measures_per_day : Seq[Seq[Int]]
    */
    var measures_per_day : Seq[Seq[Int]] = Seq[Seq[Int]]()
    val n_days : Int = measure_per_hour.length / 24
    for (day <- 1 to n_days) {
      val measures_of_day : Seq[Int] = measure_per_hour.slice((day - 1) * 24, day * 24)
      measures_per_day = measures_per_day :+ measures_of_day
    }
    return measures_per_day
  }

  def print_measures_per_day(measures_per_day : Seq[Seq[Int]]) : Unit = {
    for (measures_of_day <- measures_per_day) {
      measures_of_day.map(x => print(x.toString + "; "))
      println()
    }
  }

  def negative_to_positive(x : Int) : Int = if (x > 0) x else -x

  def filter_measure(measure : Int) : Boolean = {
    if (measure > 15 && measure < 25)
      return true
    return false
  }

  def max_measures(measures_x : Seq[Int], measures_y : Seq[Int]) : Seq[Int] = {
    if (measures_x.length > measures_y.length)
      measures_x
    measures_y
  }

  def main(args : Array[String]) = {

    val my_random : Random = new Random(42)

    val measure_per_hour : Seq[Int] = Seq.fill(336)(my_random.nextInt % 30)

    val measures_per_day : Seq[Seq[Int]] = get_measures_per_day(measure_per_hour)

    val measures_per_day_cleaned : Seq[Seq[Int]] = measures_per_day.map(_.map(negative_to_positive))

    val measures_per_day_filtered : Seq[Seq[Int]] = measures_per_day.map(_.filter(filter_measure))

    val best_day : Seq[Int] = measures_per_day_filtered.reduce(max_measures)

    val best_day_average : Double = best_day.reduce((x, y) => x + y) / best_day.length.toDouble

    println(s"best_day_average: ${best_day_average}")
  }
}