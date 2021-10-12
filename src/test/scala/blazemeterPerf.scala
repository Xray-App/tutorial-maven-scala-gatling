package performance

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class MySimulation extends Simulation {
    object Login {
        val login = exec(http("Access Reserve").post("http://blazedemo.com/reserve.php")
        .formParam("""fromPort""", """Paris""")
        .formParam("""toPort""", """Buenos+Aires"""))
        .pause(2, 3)
    }

    object Reserve {
        val reserve = exec(http("Access Reserve").post("http://blazedemo.com/reserve.php")
        .formParam("""fromPort""", """Paris""")
        .formParam("""toPort""","""Buenos+Aires"""))
        .pause(2, 3)
    }

    object Purchase {
        val purchase = exec(http("Access Purchase").post("http://blazedemo.com/purchase.php")
        .formParam("""fromPort""", """Paris""")
        .formParam("""toPort""", """Buenos+Aires""")
        .formParam("""airline""", """Virgin+America""")
        .formParam("""flight""", """43""")
        .formParam("""price""", """472.56"""))
        .pause(2, 3)
    }

    val httpProtocol = http
        .baseUrl("http://blazedemo.com")
        .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        .doNotTrackHeader("1")
        .acceptLanguageHeader("en-US,en;q=0.5")
        .acceptEncodingHeader("gzip, deflate")
        .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20100101 Firefox/16.0")

    val loginUsers = scenario("LoginUsers").exec(Login.login)
    val reserveUsers = scenario("ReserveUsers").exec(Reserve.reserve)
    val purchaseUsers = scenario("PurchaseUsers").exec(Purchase.purchase)

    setUp(
        loginUsers.inject(atOnceUsers(10)),
        reserveUsers.inject(rampUsers(2).during(10.seconds)),
        purchaseUsers.inject(rampUsers(1).during(10.seconds))
    ).assertions(
        global.responseTime.percentile(90).lt(5000),
        global.failedRequests.count.lte(0),
        global.requestsPerSec.lt(500)
    ).protocols(httpProtocol)
}


