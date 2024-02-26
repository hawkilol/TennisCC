# Motivation
- Find way to decrypt AO open infosys CourtVision API [CourtVision Data](#Data) response
- (AO page example)[https://ausopen.com/match/2024-jannik-sinner-vs-daniil-medvedev-ms701#!infosys-3]
# Discoveries
- CourVision Data js Property (Might be able to scrap indirectly via website using the div.CourtContainer properties ) ![[Pasted image 20240226170430.png]]
# Notes:
- Maybe AES encryption (CBC key)
- !REACT_APP_ENCRYPTION_KEY: "ITP2021ATP!",
- this.decrypt = function(e) {
                return im().AES.decrypt(e, "ITP2021ATP!").toString(im().enc.Utf8)
            }
- html line 477 vue data table

# Maybe useful
- 78788: function(e, t, n) {
            "use strict";
            var r = n(99410).default
              , a = n(61355).default
              , o = n(89282).default;
            Object.defineProperty(t, "__esModule", {
                value: !0
            });
            var i = n(23332)
              , s = n(84420)
              , l = function(e) {
                var t = (new Date).getTimezoneOffset()
                  , n = new Date(e.getTime() + 60 * t * 1e3).getDate()
                  , r = parseInt((n < 10 ? "0" + n : n).toString().split("").reverse().join(""))
                  , a = e.getFullYear()
                  , o = parseInt(a.toString().split("").reverse().join(""))
                  , i = parseInt(e.getTime().toString(), 16).toString(36) + ((a + o) * (n + r)).toString(24)
                  , s = i.length;
                if (s < 14)
                    for (var l = 0; l < 14 - s; l++)
                        i += "0";
                else
                    s > 14 && (i = i.substr(0, 14));
                return "#" + i + "$"
            }
              , c = function(e, t) {
                var n = l(new Date(t))
                  , r = s.enc.Utf8.parse(n)
                  , a = s.enc.Utf8.parse(n.toUpperCase());
                return s.AES.encrypt(JSON.stringify(e), r, {
                    iv: a
                }).toString()
            }
              , u = function(e) {
                var t = l(new Date(e.lastModified))
                  , n = s.enc.Utf8.parse(t)
                  , r = s.enc.Utf8.parse(t.toUpperCase())
                  , a = s.AES.decrypt(e.response, n, {
                    iv: r,
                    mode: s.mode.CBC,
                    padding: s.pad.Pkcs7
                });
                return JSON.parse(a.toString(s.enc.Utf8))
            }
- 

# Data 
- https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/belowCourt/year/2024/eventId/580/matchId/MS701/pointId/0_0_0


- https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/belowCourt/year/2024/eventId/580/matchId/MS701/pointId/0_0_0 :

- {
    "lastModified": 1708899960818,
    "response": "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"
}



# Env?

 NODE_ENV: "production",
                PUBLIC_URL: ".",
                WDS_SOCKET_HOST: void 0,
                WDS_SOCKET_PATH: void 0,
                WDS_SOCKET_PORT: void 0,
                FAST_REFRESH: !0,
                REACT_APP_NAME: "",
                REACT_APP_VERSION: "1.0.144",
                REACT_APP_API_HOST: "https://itp-ao-sls.infosys-platforms.com",
                REACT_APP_API_TELEMETRY_HOST: "https://itp-ao-sls.infosys-platforms.com",
                REACT_APP_UI_CONTEXT: "/itp/prod/ao",
                REACT_APP_FEATURE_URL: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre",
                REACT_APP_GA_CODE: "G-2M7X6VD4SL",
                REACT_APP_API_TELEMETRY: "/v1/telemetry",
                REACT_APP_API_S3_MATCH_BEATS: "/static/prod/match-beats/#year/#eventId/#matchId/data.json",
                REACT_APP_API_S3_STATS: "/static/prod/stats-plus/#year/#eventId/#matchId/keystats.json",
                REACT_APP_API_S3_RALLY_ANALYSIS: "/static/prod/rally-analysis/#year/#eventId/#matchId/data.json",
                REACT_APP_API_S3_STROKE_SUMMARY: "/static/prod/stroke-analysis/v2/#year/#eventId/#matchId/data.json",
                REACT_APP_API_S3_COURT_VISION: "/static/prod/court-vision/#year/#eventId/#matchId/data.json",
                REACT_APP_API_MATCH_STATUS: "/prod/api/match-beats/status/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_MATCH_BEATS: "/prod/api/match-beats/data/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_MATCH_BEATS_QUIZ: "/prod/api/match-beats/mbquiz/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_STATS: "/prod/api/stats-plus/v1/keystats/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_KEYSTATS: "/prod/api/stats-plus/v3/keystats/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_YTDSTATS: "/prod/api/stats-plus/v1/ytdStats/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_STROKE_SUMMARY: "/prod/api/stroke-analysis/rally/v2/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_TRN_INFO: "/prod/api/court-vision/tournamentInfo/year/#year/eventId/#eventId",
                REACT_APP_API_COURT_VISION: "/prod/api/court-vision/year/#year/eventId/#eventId/matchId/#matchId/pointId/#pointId",
                REACT_APP_API_BELOW_COURT: "/prod/api/court-vision/belowCourt/year/#year/eventId/#eventId/matchId/#matchId/pointId/#pointId",
                REACT_APP_API_RALLY_ANALYSIS: "/prod/api/rally-analysis/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_HEAD_TO_HEAD: "/prod/api/head-to-head/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_HEAD_TO_HEAD_COMPARE: "/prod/api/head-to-head/year/#year/eventId/#eventId/player1/#player1/player2/#player2",
                REACT_APP_API_INSIGHTS: "/prod/api/assisted-journalism/insights/v2/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_SOCIAL_HEATMAP_TWEETS: "/prod/api/social-heatmap/tweets/year/#year/eventId/#eventId/matchId/#matchId",
                REACT_APP_API_LOAD_MORE_TWEETS: "/prod/api/social-heatmap/tweets",
                REACT_APP_API_LEADERBOARD_RANKS: "/prod/api/slam-leader/ranks/year/#year/eventId/#eventId/eventType/#eventType/player1/#player1/player2/#player2",
                REACT_APP_ASSET_BASE_URL: "/itp/prod/ao/assets",
                REACT_APP_TRANSLATION: "/itp/prod/ao/assets/translations/{{ns}}.{{lng}}.json",
                REACT_APP_API_ENV_CONFIG: "/itp/prod/ao/config/match-centre/env.prod.json",
                REACT_APP_PERFORM_TELEMETRY: "true",
                REACT_APP_PID: "AO2024",
                REACT_APP_WEB_DOMAIN_IS_PROD: "true",
                REACT_APP_MC3D_3D_SESSION_TIME: "60",
                REACT_APP_IS_PROD: "true",
                REACT_APP_MC_URL_PROD: "https://www.atptour.com/#lang/scores/match-stats/archive/#year/#tournamentId/#matchId",
                REACT_APP_CURRENT_YEAR: "2024",
                REACT_APP_S3_ENV: "prod",
                REACT_APP_ENCRYPTION_KEY: "ITP2021ATP!",
                REACT_APP_CLIENT: "AO",
                REACT_APP_API_HOST_3D: "https://www.infosys.com/roland-garros/match-centre-3d.html",
                REACT_APP_MC3D_HOST: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre-3d/3D",
                REACT_APP_MC3D_ASSET_BASE_PATH: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre-3d/3D/scenes/",
                REACT_APP_MC3D_ASSET_TEXTURES_DESKTOP_BASE_PATH: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre-3d/3D/scenes_mac/",
                REACT_APP_MC3D_ASSET_TEXTURES_MOBILE_BASE_PATH: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre-3d/3D/scenes_mob/",
                REACT_APP_MC3D_API_BASE_PATH: "https://itp-ao-sls.infosys-platforms.com/prod/api/",
                REACT_APP_MC3D_3D_LINK: "https://itp-ao-sls.infosys-platforms.com/itp/prod/ao/match-centre-3d/index.html?year=#year&tournamentId=#tournamentId&matchDate=#matchDate&matchId=#matchId",
                REACT_APP_API_FEEDBACK: "/api/feedback/save",
                REACT_APP_TELEMETRY_DEBUG: "false"
            }.REACT_APP_IS_IFRAME,
            this.showBuild = !0,
            this.playerData = {
                tm1Ply1Country: "tm1Ply1Country",
                tm1Ply1Id: "not",
                tm1Ply1Name: "tm1Ply1Name",
                tm1Ply2Country: "tm1Ply2Country",
                tm1Ply2Id: "tm1Ply2Id",
                tm1Seed: "tm1Seed",
                tm1WinProb: 0,
                tm2Ply1Country: "tm2Ply1Country",
                tm2Ply1Id: "tm2Ply1Id",
                tm2Ply1Name: "tm2Ply1Name",
                tm2Ply2Country: "tm2Ply2Country",
                tm2Ply2Id: "tm2Ply2Id",
                tm2Seed: "tm2Seed",
                tm2WinProb: 0,
                tm2Ply1FirstName: "Novak",
                tm2Ply1LastName: "Djokovic",
                tm2Ply2FirstName: null,
                tm2Ply2LastName: null,
                tm1Ply1FirstName: "Dominic",
                tm1Ply1LastName: "Thiem",
                tm1Ply2FirstName: null,
                tm1Ply2LastName: null