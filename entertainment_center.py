import fresh_tomatoes
import media


kill_bill = media.Movie("Kill Bill",
						"A former assassin, known simply as The Bride (Uma Thurman), wakes from a coma four years after her jealous ex-lover Bill (David Carradine) attempts to murder her on her wedding day.",
						"https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
						"https://www.youtube.com/watch?v=7kSuas6mRpk",
						"https://itunes.apple.com/us/movie/kill-bill-vol.-1/id432516627",
						"http://www.rottentomatoes.com/m/kill_bill_vol_1/")
movies = [kill_bill]

fresh_tomatoes.create_movies_page(movies)

