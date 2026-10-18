/**
 * Prime Ingredients: put the creatives of Meta ad sets 80-87 into one folder per ad set.
 *
 * HOW TO RUN (takes about 2 minutes, from the Google account that owns the Drive folder):
 *   1. Open https://script.google.com and click "New project".
 *   2. Delete the sample code, paste this whole file, click Save.
 *   3. Leave DRY_RUN = true, pick the function "run" and click Run.
 *      Allow the Drive permission when Google asks. Open "Execution log":
 *      it lists every folder it would create and every file it would move. Nothing changes yet.
 *   4. If the log looks right, change DRY_RUN to false, click Save, then Run again.
 *
 * WHAT IT DOES
 *   - Inside the shared Drive folder, creates "Meta ad sets 80-87" with one subfolder per ad set,
 *     named exactly like the ad set in Meta, each with "Images" and "Videos" subfolders.
 *   - MODE = "MOVE" moves each file there (one copy of each file, nothing duplicated).
 *     MODE = "COPY" leaves the originals where they are and puts copies in the new folders.
 *   - File names are never changed, so Meta ad names still match.
 *   - Safe to run twice: existing folders are reused and files already in place are skipped.
 */
const DRY_RUN = true;
const MODE = "MOVE";                                   // "MOVE" or "COPY"
const ROOT_FOLDER_ID = "1ng4U0MmER_6v1NajZH-oToyrh8C4Lggj";
const PARENT_NAME = "Meta ad sets 80-87";

// [ad set name in Meta, subfolder, Drive file ID, file name]
const FILES = [
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1cswU6dq-buBJbUx5SHP_brwc8sGIXJhD", "20260921_Statics_V (1).png.png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1v0qV-i6oEDqvWrkcLQBikVIv1_ORNOZ_", "20260921_Statics_V (10).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1BKaKk6gBxsoLmJsHW2jJ3DpNvl-h7kZr", "20260921_Statics_V (11).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1DaLQRAiy5_IRte9FbJNQ5stL7WSkLrU7", "20260921_Statics_V (12).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1ZucseoVzke3E1cfvnreLRENAlIpV8Lid", "20260921_Statics_V (13).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1Smxr1pgf8HLvcMsBc0T9OAW6drpsyYCq", "20260921_Statics_V (2).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1Vel9PP6y_OTqgF5DV_NeUxslgDITK1KF", "20260921_Statics_V (3).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1zrkf1T3JdLEcvQsRNJ2tW8IiGq78J8qX", "20260921_Statics_V (4).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1fy3ekVJxJpbnbhNFc8klCZ0D4VxvM9wz", "20260921_Statics_V (5).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "13aNGyuqGaMIz4LLXCXvfyGYXbxbA31ce", "20260921_Statics_V (7).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1jI0tKD7OX-FBhds_KNWPAcUxpCzFF1-i", "20260921_Statics_V (8).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1iOSUCxvaZkRTXwILhWTxxXbusXRLsnOu", "20260921_Statics_V (9).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Images", "1YlZFEthFolCpzBoTw_doPMHIhC5aLTm8", "CC    20260921_Statics_V (6).png"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1iBgSUQqoMxX9EXzoQ7KikeNoxOm9oDaz", "20260921_BestDuo_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1X0XCcp6KojaGnz-DWKHUbVKTz94mM1qg", "20260921_Buy1Get1Free_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1jaU8zJFD0vXnl_y36cID4roxfAFho8TG", "20260921_DailyRoutine_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1nTrGAQVYvtQ3mihYfhEA1MFManp8HLmG", "20260921_Exposed_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1pKJ54vZD0LJTAVAGj1XWy8f_P1nnGS54", "20260921_Exposed_V2.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1kXSGT7Qtef1Xh4VmIheSRTa-HrXMUWRM", "20260921_HavingtoGrab_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1uE7oFr_FNmyXnslRenBEo2Hv4PiBEL0w", "20260921_JustSaid_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "13UY6g2srtNkv_6gxj_OAfXpRK9s3sDL_", "20260921_OldLooksYoung_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1kxjZCHwDMci70steBcw2akNaihv_QFXx", "20260921_Podcast_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "15U0S2vBviK-5bVQWbXgEjXGQzRXsQFBp", "20260921_Recovery_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "15c7o_0Xh8w2LhfyzrJMA6wUXnpbww69H", "20260921_SideEffects_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1MNrDit31Gy574lsKQNVkICQhWcSBMdWL", "20260921_TheFix_V1.mp4"],
  ["80__Broad_USA_Creative_testing - 14-10-26", "Videos", "1sTLQPNHGxBUlSO-q6dlhVTsJEYDxUgFl", "20260921_UniverseSign_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1j-MuN5kQrceHfQZ2D1SkfJbPFZvGF2cW", "20260924_Static_V (1).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1tKliltsglFNc4l2qS0bIgl-tJMMmag_L", "20260924_Static_V (10).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1tIppbcvlX_IHvygMSpK4RNDavdCcjgew", "20260924_Static_V (11).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1L--HeNzhtD3H-s8yXl6O884LZyenocu8", "20260924_Static_V (2).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1ZGcJ83BaihPdAJazjETqFZLU-grsKdht", "20260924_Static_V (3).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1A1AJpNKqeuE-nH7qBp0GN-T1apB21nx3", "20260924_Static_V (4).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "180_ALVwxPpLIYHDabOZ_KNBQ5bWm4chX", "20260924_Static_V (5).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1BDJgfhQCZZyqFksisSRmPL7GLa93u-iM", "20260924_Static_V (6).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1dTxwx_Yf3IyKz2PfETcksbaIVp-ZPpN0", "20260924_Static_V (7).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1gJqCbKZrVCp9GZAT2SSu-YqTcw6QerYC", "20260924_Static_V (8).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Images", "1xx54t6nn2cjWjjS7i1FPWSd7qC9qLPte", "20260924_Static_V (9).png"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1Whsr4Fk3oT8jdxYYD8HPQ3Dd9_q6gwvp", "20260924_42%WomanFaceThis_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1iBZR6E2-4ObjRUTBVnXjx0xUAjE6H1Wj", "20260924_90dayNMNResult_V2.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1qEG0aTLuhC8XRhitJI6Po_nTEsFSxvWS", "20260924_DocMDAdvice_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1lXfB2XnJgXs2inWMuo_Qgkrp8KvuJihi", "20260924_DontMissTheStep_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1T3m16ZDNvSmSUnjqFezhOTKYF1_LxCwH", "20260924_DoubleDiscount_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1-fGFo5uI6vFSrjbmB1tns07PzrK0c-gV", "20260924_FallEndSale_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1asU_C6L9bLVYJTHyy3XGCvOAWsGVBUiU", "20260924_FixedSkinForever_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1XwMg11DY_ifr87hLa9xqGsgjx3-dOH0z", "20260924_LastDayofCrazyPriceDrop_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1jfT5dX8BkJbteCuw9W4A17yKQB4tbxsR", "20260924_NADPeopleDidnotTellYou_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1ER2qh1wwRnh_n8RB_96E9b54XdeRFgSg", "20260924_OnSaleNow_V2.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1vUOhlFILct4o_3XFxHThIgXaAeY0Qd25", "20260924_PodcastExplainer_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "159luRw5iE9mprZKMDbX2bpRrWQPK9-cu", "20260924_Reviews_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1G_2xuzAsWdrkbfYEhTaL25TAJrihAIhl", "20260924_ShoelaceExplanation_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1X5QxmuCeI6sd7rUabezjsxZFTBrvUysX", "20260924_TFixInsulineProlem_V1.mp4"],
  ["81__Broad_USA_Creative_testing – 16-10-26", "Videos", "1jJif9dPmbNl23oMjSv9M2QGS7zqSlGOw", "20260924_USGovUsesNMN_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "12at1S1j6pjkknqEykHzei_epD1fby3HI", "20260928_Static_V (1).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1LMqrqxyTm6HBaDCik-e23ReYtUskeTt8", "20260928_Static_V (10).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "18IDO5GfLmvYIw5GqV7e4VaD7VzYoyqAv", "20260928_Static_V (11).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1t4lML1io1IzftGzI6TfzoP2THXiWCCr7", "20260928_Static_V (12).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1nzurP-nWB7-UA0IexckFpGkN2EqVS1Ft", "20260928_Static_V (13).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1Z09c0hUzGplwh3pMVM95iY3Bz4vUG3CN", "20260928_Static_V (14).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1c14rEdsXOYz0-jx7ph_Dl2aZCZci78Ii", "20260928_Static_V (15).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1Oiap1zxZnukon7MJeSU3P-za6rowyCwf", "20260928_Static_V (2).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1ETztsH-mcicDXLI6-SKwqgGdqu5d8U4Q", "20260928_Static_V (3).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "19e84ZUVJxAdvhMndwBdnrU-8VsSPmxSD", "20260928_Static_V (4).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1doZKnNbZrlSahjYmI_HbgxtGvO34Bncz", "20260928_Static_V (5).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1Xy5oUM01Dk0aeGYEeOgmQvCz1HW2MxfC", "20260928_Static_V (6).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1TxuBasQoAvKIpcAlBFwhmR2v-6xhW5-q", "20260928_Static_V (7).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1qbGl-v0prf9SwrimwY9vhw0xlOdSg4Lx", "20260928_Static_V (8).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Images", "1Qsz0BLHHK3A972ifPWepCnPxd8hYYxcw", "20260928_Static_V (9).png"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1QXkHPCz-Uy7PyERLx1Yne9pRqTyapTFI", "091520260928_HollywoodStars_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1FU6ckgGMdu07UNWvOFNay8pRFztq4qLo", "20260928_DontTakeNMN_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1jBiC2kaLOUhBcKteb0DCvIvyZ7-f5NGq", "20260928_DontUseNMN_V2.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1Ivq9-kEn0VXKsK8FxJtwD9CERCGwjOGt", "20260928_DontWasteMoney_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1F6o7oE_xIGN0cNqmdwYZZsxwnMuulqyr", "20260928_DontbuyNMN_V2.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1ks7r2FeuU8CKRPUsmtrJW2iWjZORW1Jw", "20260928_FixAging_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "13VVEljxnJFQvdhqInno5gixaVVoKKWzz", "20260928_HowIChanged_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1N8qD3kFH-x54MEjgwcuwokjk6UZ7y2Uh", "20260928_ItsNotPlasticSurgery_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1AoBjxb3levW9O6Pl8HXMTTKG2MVf_8zR", "20260928_LintenToThis_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1sgj7h1BS520IOn5XA95oKhl730Xs0W6U", "20260928_NMNBanned_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1VceEr7xSKJkDjqQxYeMUX_zT5cydNmsH", "20260928_RealNMN_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1fXargApanznTUHT-D7-xv703CyNiW1nw", "20260928_RequiresNMN_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1UBREbwAZ9F3HRgjTF1xUKy-mC1n0khWo", "20260928_SheSaysThat_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1s61VuKwd8ZWj3IEzne4JAksb6DMe18qn", "20260928_SupplementScama_V1.mp4"],
  ["82__Broad_USA_Creative_testing – 18-10-26", "Videos", "1Xoxw2KABK2KpoI6-wZUStggSZHjk6boW", "20260928_YoungGrandma_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1vGkkVih_8QijtuvVh_rz2NTUIWk1SDCW", "20260929_Static_V (1).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "16aCFgt3C-xvbLzsfKLBv_h9HAazBqLf_", "20260929_Static_V (10).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1iEF8wsCViHKynD_XyDLZHsBKbMLzn05V", "20260929_Static_V (11).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1T6lnJnfdKlJw9ivL0ys6kUMTpLekUbng", "20260929_Static_V (12).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "16gKaYFnHXl_tG_9cW9AYVZwScvt5WfcW", "20260929_Static_V (13).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1PDzX2D21gLSxzClc4nvjthivALTDeVzD", "20260929_Static_V (14).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "14EfqkL6HAk6NE4WQg6oUg7Id-mmsORRN", "20260929_Static_V (15).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1gh48sDW0R0ekrbAwLFJq79SgygWdvIzE", "20260929_Static_V (2).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1cY5gwB2OSUrId31MyAd1I2fmTjeZ9_ri", "20260929_Static_V (4).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1hFM-_m29otZZvBevMvZH5TibpJ_wSzCI", "20260929_Static_V (5).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1VH0UFsJ6zMdEveGHeVci55WI43vu2Fuu", "20260929_Static_V (6).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1ZFzs7dt8IooGTeDDL2mBgMFQzs0WTl-C", "20260929_Static_V (7).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1sVkncWG1G7KjkQz477iHl4yVpnYCu0Q8", "20260929_Static_V (8).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Images", "1jGG7MhECLswbOh1sOLPlhuOADXhoSgQT", "20260929_Static_V (9).png"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1KUZK2Fylm1Io-vHq4qLpqZl6wL0HL7Wn", "20260929_AfterEffects_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1lZFn0DBrWHZJastzi0hZPQX3haDbfcNw", "20260929_Bandaid_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1HlnXO0JDiOJmi1_j3-3g0gvbvlOi1O88", "20260929_Biology_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1JNIumiq8g5xskxj2mS3m38izZGnvuSgr", "20260929_BrayanJ_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1VIFZRVXgtMolgJwpFa2rQQdThV_qUNVq", "20260929_Exposed_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1rhOTrczvafSWmwRoYI8w7jDmIGfqd25x", "20260929_LiveTV_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1GY8n7r0Q2T0awdn4-BW5aBTXKwV5tgJS", "20260929_PlasticSurgery_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1pBJcZb9F9m46xapm8Z9b3G0AiZ5kJVMu", "20260929_RightWay_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1-BSfRt1CbByDOOx6JN1ro7CeJvLhVYF3", "20260929_SaleEnds_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1B14waxE3H7kc-L0arjOdc41BKWuIbO57", "20260929_Scam_V2.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1TWJ0eg6WKaJVIN5GGCvhyL-xmQ2jpTIq", "20260929_TScore_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1jEsr8AuGSIMXmg7jC5YVSU1-dNepgf9R", "20260929_TakeDown_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1ISApKU45llV7zVrzXHK7tfqBmeOjtJzX", "20260929_TakeEveryday_V1.mp4"],
  ["83__Broad_USA_Creative_testing – 20-10-26", "Videos", "1B8D_wRPIyMGBjVK9CB9TgB0Qb0fuylOh", "20260929_ThisToThat_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1iN02pWCzC8V_dPri8o8DcJDaCdGE2GGw", "20260930_Static_V (1).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1UpBAP58yQFo7wx3Lmg-9UKG-n7RYUhIU", "20260930_Static_V (10).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1rOxhvEejhnqbIYHDrOpFix9f-Kga6nkn", "20260930_Static_V (11).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "18ijwzQ7wBF4Agtn3UN88I3vasPCIh0Zx", "20260930_Static_V (12).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "16PM_zVoBoNUdRLPdfo3qPE0rW7HTLvm-", "20260930_Static_V (13).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1Tam-y_zlAF2JEWu8BJ1WXNXsgr9Cn_4N", "20260930_Static_V (14).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "19Eg-JageOmbJ8oyvq8-EubXrCdoXwqjp", "20260930_Static_V (15).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1IB2jnPic-9rNIdSIePev9SoFJJN1KhxQ", "20260930_Static_V (16).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1wyi9Iu89E6mlIK6ifSNpC26ootnxO1LV", "20260930_Static_V (2).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1wZnNqeIN0CAtXx_oYLEbMj0vt-mFj4gp", "20260930_Static_V (3).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1ZRzjXygi9Yj-saRZoOjXuwKLfypRIruD", "20260930_Static_V (4).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1N7O5Sa44Q2PxG0U4HLrFNgmvSt1DlyUu", "20260930_Static_V (5).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1QskKIJlaN05Uqk1ukhK1m0GV7JQMz3Hh", "20260930_Static_V (6).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1VOOJb1zLyPl5bbarfIS4DCTtWesp_bwT", "20260930_Static_V (7).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "1_9gB70KMflARqlpP1gtrQnf4swGX7k8c", "20260930_Static_V (8).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Images", "13npypc-g-xeaPKf-PqfYQhTv7LQg9hrM", "20260930_Static_V (9).png"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1l1tXaOlrn2tkp2zPNXFTU1tFQR5cvw3G", "20260930_2For2_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1WGzXy7x6wY9syFxFmUaqPsXpvVrueEUV", "20260930_Deal_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1WKsdxaDqvjnEw3qHtwcdeg6QX03QsUEn", "20260930_Decode_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1uTq8vDAIBIwjUFOPxDVhaJdAchckUZJn", "20260930_FlashSale_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1wJUsglCHAdLUQCYPww4Grn9EFGSeyosF", "20260930_GotoBundle_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1QP3OdTz3ay8EWEAkn4oOGpxKLZDaKLGV", "20260930_GrabIt_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1ZFi-oUWAhDUhsDjK_VyFzamldQs56Klr", "20260930_ItsCrazy_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1jfX2fZqKlDJRHvBDbyp0fllTmJXNPhp1", "20260930_MeetNMN_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1tmohXNWD3nM_0PWEkHfXIgpzqmRNalCj", "20260930_MorningFirst_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1V7E1qn5_5ALVl-LA0QPJ-y6h8dDZJFkT", "20260930_NMNvsAstaxanthin_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1qJamMV-D1qM-hxHLVNf2rvETZTKxFR8N", "20260930_PriceDrops_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1qjmyhXN6ye5iRym_2_6Zf1rJod-VTI8g", "20260930_TapTheCart_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "17aq7Si14xiy-nXhHbCjhR3C-lFI1Dxe2", "20260930_TheOne_V1.mp4"],
  ["84__Broad_USA_Creative_testing – 22-10-26", "Videos", "1WXSd925vjtQ6heGSbwkaA1DKciGp8daz", "20260930_Truth_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1FnfIgya0V5MPlGWrXqMd1QS1YS2iOJDO", "20261001_Static_V (1).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1Vkxhapzr8nq3WdmZXP5kduA0SBeYVS65", "20261001_Static_V (10).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1at67r-kzM7RTBZM-bK4F5eKFz1IfWJxw", "20261001_Static_V (11).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1YvN0KE_Ss7G6b3JF5APe3RPfV1W0rsGy", "20261001_Static_V (12).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1tmR8KaiRLXmNm8YvkHJbPncQnZVP90ip", "20261001_Static_V (13).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1xy95LW8-giir-u0tj6Nv2y2-FIdM18fr", "20261001_Static_V (14).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1cClBe0-5-2FWsV6W-3CeopyKdHsT2T2L", "20261001_Static_V (15).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1xICzh5mi8Q-5IiZBtZ-rQki9haUuN0p6", "20261001_Static_V (2).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1vFWtmkyvh9G1uMDOmuM1urU7rkmhQN9T", "20261001_Static_V (3).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "11ZPiJ7Sj9Ynq2jVRUAZF_6eEehgsVLCz", "20261001_Static_V (4).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1I3lfCPNZ5c7ysQU29EBVBo9JExjFcLhN", "20261001_Static_V (5).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1ijbe-lZFrW7pu_ZmG7QNUbTkJhJYCMfQ", "20261001_Static_V (6).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1xZmF2YMrRKMn0ZpNJpgpO0wpGx-ODZsi", "20261001_Static_V (7).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1sePNb2afpDteIEsLcrSo5ByKdtzVAUWi", "20261001_Static_V (8).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Images", "1lEr1VNzqvkRWiSUjlgza8RGOvzsGMuXr", "20261001_Static_V (9).png"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1MAgLltzr-foeN3BheuKC3MnhWyc0j2iK", "20261001_6MonthsJourney_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1PIgz5vlt27RfGZjdvobMAAAcUfllUeIj", "20261001_Athletes_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "15GugcDTUdD6c4A_BP2YfAAOo1kcvPJyr", "20261001_BiggerThanCreatine_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1PW-VgQZ4bzr4oothJT9nwqOx_og0whOC", "20261001_DoubleDiscount_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "14ucFaeMjU46vS5rd2ncCm_k6zO6HzJfQ", "20261001_EyeSight_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1F3pMhtILAuMox7bNAQr6fOg7WKCyDGbY", "20261001_HairGoneBack_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1B_j4R4wz5BsXfOalgBeQycifcZKQF4Yl", "20261001_Longevity_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1XgFz7cp4XJFu43i_VztM46uKn9w6zoRM", "20261001_NADvsNMN_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1UevcriIOASEwCXlzjTZunuTHl2u_AWjc", "20261001_Over50s_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1J5dBW2_kYaZyMBFdwFgrkjxz0D_50Xgc", "20261001_Podcast_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1VSfCehm3lXTJSp_UJgDbzpU95s4UFtcZ", "20261001_QuestionToLongevity_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1H0OSaY5ez5q1E4Oov4cOaMX3ChqhVTi_", "20261001_ReverseGrey_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1VBfv0ZU4az3ldc35o-k4rayZvqnz6CqE", "20261001_Rightway_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1rjPRfDvJ9AUfDxC3xzjC5zONaP9Flfnv", "20261001_Secret_V1.mp4"],
  ["85__Broad_USA_Creative_testing – 24-10-26", "Videos", "1hyxl-yTaDHPp91BVcE4Bp9d8xTULXqFh", "20261001_StopTaking_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "18Qfa-NkVPj41xzDGrPUoaMbtxKZ-4Md9", "20261002_Static_V (1).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1yYM5OfOz-sHSwiFLtQpRJ4mmucRJJq2g", "20261002_Static_V (10).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "195-M3cSgVLeyq9OEWe2CHZ-QHDY2Y4Es", "20261002_Static_V (11).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1uyKeBePgED9Kle_OChh6ybayRWqR1lZR", "20261002_Static_V (12).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1M5IMV_CRaUbAFmcr7q2kWBMam-iySGj0", "20261002_Static_V (13).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1dIhrya5zm6Zv8YuvjVUcDfzSuZnaQb85", "20261002_Static_V (14).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1Eb6ruBx5WlZwZUBmmrEyHoKXYmUaZ68H", "20261002_Static_V (15).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1elz9qWk_l2JHPaI_80sQT1JmAL55xPHt", "20261002_Static_V (2).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "19qV61dyR7Swq-hjAhwtKoS1OZeuevgXb", "20261002_Static_V (3).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1tihjBaCqDEzYJ_UbGJ_u_VI4UVR6v-Yg", "20261002_Static_V (4).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1MK6TtJRlVdgwOj4v6WskM3qMxm1io50n", "20261002_Static_V (5).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1CCIsTbg1Eq902E67xbylm-df2f--Ogw0", "20261002_Static_V (6).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1qBUv-HNoELPf5lv0HPE-36BnpMCa8w2L", "20261002_Static_V (7).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1NCpvxF8-ZioRkSBzbukEs9q4qOCYhfGI", "20261002_Static_V (8).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Images", "1Y-_t3WQafOCiW2R-vyY61x2l-YJKDR_Q", "20261002_Static_V (9).png"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1xwhzScu5tUdoJn-ajHEbChHIScb7mPXo", "20261002_Animated_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1Ntc98NEaY0cqjyxv8E2lPnTJV5rAd9PH", "20261002_CaptAmerica_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "16EMMnfe0Oc9ugrDgxDPka2pgghCCREzq", "20261002_CarExplained_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "14CIXPhVEBkEOI2XD7I8Gfq8kqsgQx41T", "20261002_CarExplained_V2.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1kuuEw-7qOVHeRb2gNyzPWGi0D8jfdlWS", "20261002_Checkout_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1PDz5igWPFClgXYCgDivvNVkxRQROPi4h", "20261002_CoffeeAin'thitting_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "132ft8kgaf9soU1S3u7tKVgr5Lc7nUfzL", "20261002_DoctorAdvice_V2.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1mwisqdSy4yYs7tJuZkZ6PjL9fypl3943", "20261002_FlashSale_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1KbOARcM9FJ9cDo73eMIs2GiNp6uHfRWy", "20261002_IDontLook40_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1c9_LZurpGQJqLV-Sdy5MrHAhvqMRsZP0", "20261002_ILoveNMN_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1L_fOCgefrfbQgyOgfueyYe3xJinKHEHI", "20261002_MassiveSale_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1RfpfEz2MDfM_66YO601QZQmTb6vT8vk8", "20261002_MenopauseWomen_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1vOgGyMkM_SH6njuaK2evxM7UfZTpA_7z", "20261002_NMNVsNAD_V2.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "1dRBHYLiCPNTPD2tIeVdRanBM-juylY2y", "20261002_Older_V1.mp4"],
  ["86__Broad_USA_Creative_testing – 26-10-26", "Videos", "18ejYPsb3BmvX3qPi4zNl4Ckrqe_4YEF-", "20261002_Teacher_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1bNhTN6M08AxFMWJAYjgFFZf8ehi2SF_h", "20261003-Static_V (1).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1PNqiEtFVUSB_ZADXheTfmgMUn6vgyFOY", "20261003-Static_V (10).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1e3PKkJWbVv7MG26jiMe_GrZaByUbqQjb", "20261003-Static_V (11).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1YwFmKhwcI2d8nzCvDrmXoLvRpMINBCrw", "20261003-Static_V (12).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1nn9dO1U3N7IEZNnpnpbch651ZlFEhZ6U", "20261003-Static_V (13).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1SN4GYY19o6Dy865Tgo3_8FLa07K5GXtY", "20261003-Static_V (14).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1G7lfDoVE_GwObo96_EHD5CwzA8vRopRk", "20261003-Static_V (15).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1iBgU9zLmQwCDKAv7GxG_9cQxxo-XYA0W", "20261003-Static_V (16).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1gePWoQRmhdpb7yfQhKVkbqXIILFoq6zI", "20261003-Static_V (17).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1kkDq_nKKwsChjasDDspvCZk24pABbhzs", "20261003-Static_V (18).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1Oy7I_IJ7TGnKCV7psx6Y2d4LRn0riUYy", "20261003-Static_V (19).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "19VsyY1ZajBLqtsds7m-JUPpeALYgyasa", "20261003-Static_V (2).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1j-TrNIPQndkVqekGeko0lFFCDCIwQOlH", "20261003-Static_V (20).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1Amb0PiLtqS9a-pNTljwxyrqfqhSvr7vf", "20261003-Static_V (3).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1pJQBpzXgs8UmRWSeoTjo-MY5hYUUgJ-J", "20261003-Static_V (4).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1MmsGV0C8B871evAA5hsjpGGkuMsdBcGb", "20261003-Static_V (5).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "19N7vRUBFcxhTOI3uVNbWHs3AorHXHydE", "20261003-Static_V (6).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1EPf-lRzJ8EscTiLvtSB3Hajw726Ufk1v", "20261003-Static_V (7).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1Chv7NLtMKd2dx5Fk0ABtyzlXMfynTVlA", "20261003-Static_V (8).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Images", "1UAtFwXblnIniMmpB-ZujpoXv7onzMkfa", "20261003-Static_V (9).png"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1KpPz6GKHC57KKGPgkXJwNM_WYdPa9ucX", "20261003_61yrNMNefferct_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1IubOzuSIk88rlSD51105oOz63jxWlGAO", "20261003_BiggerThanCreatine_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1Y-Sx-K-mhueqVzccBNHOXohCKtsmoArf", "20261003_EndsToday_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "17RpatPt0NiyhJuANpQ56j3nu4fI7GQw6", "20261003_Explainer_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1JOt7iMt5XsMXLyGkHPrv0OLRnBLfHrj0", "20261003_GetThisTonight_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1cPmH-h9ZhOZBz2PUHhTRF2nmsZOnkRQb", "20261003_HonestReviews_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "141axdEDzNpgE7gqHttdSx6pIKoB4-d0L", "20261003_Iam40_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1jVCfVMBmyE5hCG2aqPuFa81vkdx_ozCI", "20261003_NADorNMNt_V1.mp4"],
  ["87__Broad_USA_Creative_testing – 28-10-26", "Videos", "1QUTA8I7kV2EV-1JJOQHNYlFwJTqDrKsj", "20261003_Tedtalk_V1.mp4"],
];

function getOrCreate_(parent, name) {
  const it = parent.getFoldersByName(name);
  if (it.hasNext()) return it.next();
  if (DRY_RUN) { Logger.log("would create folder: " + name); return null; }
  Logger.log("created folder: " + name);
  return parent.createFolder(name);
}

function run() {
  const root = DriveApp.getFolderById(ROOT_FOLDER_ID);
  const parent = getOrCreate_(root, PARENT_NAME);
  const cache = {};
  let done = 0, skipped = 0, failed = 0;
  FILES.forEach(function (row) {
    const adset = row[0], sub = row[1], id = row[2], name = row[3];
    const key = adset + "/" + sub;
    if (!(key in cache)) {
      const a = parent ? getOrCreate_(parent, adset) : (DRY_RUN && Logger.log("would create folder: " + adset), null);
      cache[key] = a ? getOrCreate_(a, sub) : (DRY_RUN && Logger.log("would create folder: " + adset + "/" + sub), null);
    }
    const dest = cache[key];
    try {
      const file = DriveApp.getFileById(id);
      if (file.getName() !== name) Logger.log("NOTE: name differs, expected '" + name + "' found '" + file.getName() + "'");
      if (dest && file.getParents().hasNext() && file.getParents().next().getId() === dest.getId()) { skipped++; return; }
      if (DRY_RUN) { Logger.log("would " + MODE.toLowerCase() + ": " + name + "  ->  " + adset + "/" + sub); done++; return; }
      if (MODE === "COPY") file.makeCopy(name, dest); else file.moveTo(dest);
      Logger.log(MODE.toLowerCase() + "d: " + name + "  ->  " + adset + "/" + sub);
      done++;
    } catch (e) {
      failed++;
      Logger.log("FAILED: " + name + " (" + id + "): " + e);
    }
  });
  Logger.log((DRY_RUN ? "DRY RUN. " : "") + "files: " + done + ", already in place: " + skipped + ", failed: " + failed + ", total planned: " + FILES.length);
}
