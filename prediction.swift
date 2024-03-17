//
//  prediction.swift
//  bulk
//
//  Created by Ryan on 3/13/24.
//

import SwiftUI

struct prediction: View {
    @Binding var goal: String
    @Binding var c_in: Double
    @Binding var c_out: Double
    @Binding var protein: Double
    @Binding var steps: Double
    
    var body: some View {
        NavigationStack {
            ZStack {
                Color.blue
                    .ignoresSafeArea()
                Circle()
                    .scale(1.7)
                    .foregroundColor(.white.opacity(0.15))
                Circle()
                    .scale(1.35)
                    .foregroundColor(.white)
                VStack {
                    let netc = c_in-c_out-1700
                    let scal = steps/100
                    let net = Int(netc-scal)/10
                    let surplus = netc > 0
                    let senough = steps>=4000
                    let penough = protein>=100
                    if goal == "bulking" {
                        if net < 0 {
                            Text("Score: 0")
                                .font(.largeTitle)
                                .bold()
                                .padding()
                            Text("You are not meeting your bulking goals!\nSome recommendations:")
                                .font(.title2)
                                .padding()
                            if !surplus {
                                Text("- Consume at least " + String(Int(500 - netc)) + " more calories")
                                    .padding()
                                
                            }
                            
                        }
                        else{
                            Text("Score: "+String(net))
                                .font(.largeTitle)
                                .bold()
                                //.padding()
                            Text("\t\t\tGreat job!\nSome recommendations:")
                                .font(.title)
                                //.bold()
                                .padding()
                            Text("- Lift weights for 30 minutes")
                                .padding()
                        }
                    }
                    else{
                        if net > 0 {
                            Text("Score: 0")
                                .font(.largeTitle)
                                .bold()
                                .padding()
                            Text("You are not meeting your cutting goals!\nSome recommendations:")
                                .font(.title2)
                                .padding()
                            if surplus {
                                Text("- Run " + String(Int(netc/150)) + " miles")
                                    .padding()
                            }
                        }
                        else {
                            Text("Score: "+String(0 - net))
                                .font(.largeTitle)
                                .bold()
                                .padding()
                            Text("\t\t\tGreat job!\nSome recommendations:")
                                .font(.title)
                                //.bold()
                                .padding()
                            Text("- Do yoga for 30 minutes")
                                .padding()
                        }
                    }
                    if !penough{
                        Text("- Consume " + String(Int(100 - protein)/20*6) + " oz of chicken")
                            //.bold()
                            .padding()
                    }
                    if !senough{
                        Text("- Walk " + String(Int(4000 - steps)/2000) + " mile(s)")
                            //.bold()
                            .padding()
                    }
                }
                .offset(y: -60)
            }
        }
    }
}

#Preview {
    prediction(goal: .constant("cutting"), c_in: .constant(0), c_out: .constant(0), protein: .constant(0), steps: .constant(0))
}
