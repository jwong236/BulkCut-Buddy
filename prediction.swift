//
//  prediction.swift
//  bulk
//
//  Created by Ryan on 3/13/24.
//

import SwiftUI
import Charts

struct prediction: View {
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
            }
        }
    }
}

#Preview {
    prediction()
}
