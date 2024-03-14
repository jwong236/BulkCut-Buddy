//
//  homepage.swift
//  bulk
//
//  Created by Ryan on 3/13/24.
//

import SwiftUI

struct Homepage: View {
    @State private var showingEnterData = false
    @State private var showingPredictions = false
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
                    Image("stronk_anteater")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .cornerRadius(250)
                        .frame(width:400, height: 400)
                    HStack{
                        Button("Enter data") {
                            showingEnterData = true
                        }
                        .foregroundColor(.white)
                        .frame(width: 150, height: 50)
                        .background(Color.blue)
                        .cornerRadius(10)
                        
                        Button("Predictions") {
                            showingPredictions = true
                        }
                        .foregroundColor(.white)
                        .frame(width: 150, height: 50)
                        .background(Color.blue)
                        .cornerRadius(10)
                    }
                    
                    
                }
                .offset(y:-40)
                NavigationLink(destination: enter_data(), isActive: $showingEnterData) {
                    EmptyView()
                }
                
                NavigationLink(destination: prediction(), isActive: $showingPredictions) {
                    EmptyView()
                }
                
            }
            .navigationBarTitle("")
            .navigationBarBackButtonHidden(true)
            .navigationBarHidden(true)
        }
    }
}

#Preview {
    Homepage()
}
